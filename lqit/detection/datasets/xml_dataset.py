# Copyright (c) OpenMMLab. All rights reserved.
import copy
import os.path as osp
import xml.etree.ElementTree as ET
from typing import List, Optional, Union

import mmcv
from mmdet.datasets import XMLDataset
from mmdet.registry import DATASETS
from mmengine.fileio import list_from_file, load
from mmengine.utils import is_abs


# TODO: update after https://github.com/open-mmlab/mmdetection/pull/8893
#  have been merged
@DATASETS.register_module()
class XMLDatasetWithMetaFile(XMLDataset):
    """XML dataset for detection. Add load image meta_info to speed up loading
    annotations if the image size is not in xml file.

    Args:
        img_suffix (str): The image suffix. Defaults to jpg.
        meta_file (str): Image meta info path. Defaults to None.
        minus_one (bool): Whether to subtract 1 from the coordinates.
            Defaults to False.
        **kwargs: Keyword parameters passed to :class:`XMLDataset`.
    """

    def __init__(self,
                 img_suffix: str = 'jpg',
                 meta_file: Optional[str] = None,
                 minus_one: bool = False,
                 **kwargs) -> None:
        self.img_suffix = img_suffix
        self.meta_file = meta_file
        self.img_metas = None
        self.minus_one = minus_one
        super().__init__(**kwargs)

    def _join_prefix(self):
        """Join ``self.data_root`` with annotation path."""
        super()._join_prefix()
        if self.meta_file is not None:
            if not is_abs(self.meta_file) and self.meta_file:
                self.meta_file = osp.join(self.data_root, self.meta_file)

    def load_data_list(self) -> List[dict]:
        """Load annotation from XML style ann_file.

        Returns:
            list[dict]: Annotation info from XML file.
        """
        if self.meta_file is not None:
            self.img_metas = load(
                self.meta_file,
                file_format='pkl',
                file_client_args=self.file_client_args)
        # TODO: check whether can use super().load_data_list()
        assert self._metainfo.get('CLASSES', None) is not None, \
            'CLASSES in `XMLDataset` can not be None.'
        self.cat2label = {
            cat: i
            for i, cat in enumerate(self._metainfo['CLASSES'])
        }

        data_list = []
        img_ids = list_from_file(
            self.ann_file, file_client_args=self.file_client_args)
        for img_id in img_ids:
            img_path = osp.normpath(
                osp.join(self.sub_data_root, self.img_subdir,
                         f'{img_id}.{self.img_suffix}'))
            xml_path = osp.normpath(
                osp.join(self.sub_data_root, self.ann_subdir, f'{img_id}.xml'))

            raw_img_info = {}
            raw_img_info['img_id'] = img_id
            raw_img_info['img_path'] = img_path
            raw_img_info['xml_path'] = xml_path

            parsed_data_info = self.parse_data_info(raw_img_info)
            data_list.append(parsed_data_info)
        return data_list

    def parse_data_info(self, img_info: dict) -> Union[dict, List[dict]]:
        """Parse raw annotation to target format.

        Args:
            img_info (dict): Raw image information, usually it includes
                `img_id`, `file_name`, and `xml_path`.

        Returns:
            Union[dict, List[dict]]: Parsed annotation.
        """
        data_info = copy.deepcopy(img_info)
        img_path = data_info['img_path']
        # deal with xml file
        with self.file_client.get_local_path(
                img_info['xml_path']) as local_path:
            raw_ann_info = ET.parse(local_path)
        root = raw_ann_info.getroot()
        size = root.find('size')
        if size is not None:
            width = int(size.find('width').text)
            height = int(size.find('height').text)
        else:
            if self.img_metas is not None:
                img_meta_key = osp.join(
                    osp.split(osp.split(img_path)[0])[-1],
                    osp.split(img_path)[-1])
                img_shape = self.img_metas.get(img_meta_key, None)
                height, width = img_shape[:2]
            else:
                img_bytes = self.file_client.get(img_path)
                img = mmcv.imfrombytes(img_bytes, backend='cv2')
                height, width = img.shape[:2]
                del img, img_bytes

        data_info['height'] = height
        data_info['width'] = width

        data_info['instances'] = self._parse_instance_info(raw_ann_info)
        return data_info

    # TODO: update after https://github.com/open-mmlab/mmdetection/pull/8893
    #  have been merged
    def _parse_instance_info(self, raw_ann_info: ET) -> List[dict]:
        """parse instance information.

        Args:
            raw_ann_info (ElementTree): ElementTree object.

        Returns:
            List[dict]: List of instances.
        """

        instances = []
        for obj in raw_ann_info.findall('object'):
            instance = {}
            name = obj.find('name').text
            if name not in self._metainfo['CLASSES']:
                continue
            difficult = obj.find('difficult')
            difficult = 0 if difficult is None else int(difficult.text)
            bnd_box = obj.find('bndbox')
            bbox = [
                int(float(bnd_box.find('xmin').text)),
                int(float(bnd_box.find('ymin').text)),
                int(float(bnd_box.find('xmax').text)),
                int(float(bnd_box.find('ymax').text))
            ]

            # VOC needs to subtract 1 from the coordinates
            if self.minus_one:
                bbox = [x - 1 for x in bbox]

            ignore = False
            if self.bbox_min_size is not None:
                assert not self.test_mode
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                if w < self.bbox_min_size or h < self.bbox_min_size:
                    ignore = True
            if difficult or ignore:
                instance['ignore_flag'] = 1
            else:
                instance['ignore_flag'] = 0
            instance['bbox'] = bbox
            instance['bbox_label'] = self.cat2label[name]
            instances.append(instance)
        return instances
