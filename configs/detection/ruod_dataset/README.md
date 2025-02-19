# Real-world Underwater Object Detection

> [Rethinking general underwater object detection: Datasets, challenges, and solutions](https://www.sciencedirect.com/science/article/abs/pii/S0925231222013169)

<!-- [DATASET] -->

## Abstract

In this paper, we conduct a comprehensive study of Underwater Object Detection (UOD). UOD has evolved into an attractive research field in the computer vision community in recent years. However, existing UOD datasets collected from specific underwater scenes are limited in the number of images, categories, resolution, and environmental challenges. These limitations can lead to the settings and effectiveness of models trained on existing datasets being impaired in general underwater situations. These limitations also constrain the comprehensive exploration of UOD. To alleviate these issues, we first present a new real-world UOD dataset called RUOD that places UOD in the context of general scene understanding. The dataset contains 14,000 high-resolution images, 74,903 labeled objects, and 10 common aquatic categories. The dataset also has various marine objects and rich environmental challenges including haze-like effects, color casts, and light interference. Second, we conduct extensive and systematic experiments on RUOD to evaluate the development of general underwater scene detection from the perspective of algorithms, complex marine objects, and environmental challenges. The findings from these explorations highlight the challenges of UOD and suggest promising solutions and new directions for UOD. Finally, UOD in practice typically uses underwater image enhancement during preprocessing to improve image quality. We thus characterize object detection performance on enhanced images and find an effective auxiliary framework of image enhancement for UOD. Our dataset is available at https://github.com/dlut-dimt/RUOD.

<!-- [IMAGE] -->

<div align=center>
<img src="https://user-images.githubusercontent.com/48282753/233956427-b75dba85-96b7-4ba7-9ccb-2aa3b1847bc6.png" height="400"/>
</div>

## Results and Models

| Architecture  | Backbone |  Style  | Lr schd | box AP |                      Config                       |                                                                                                                                      Download                                                                                                                                      |
| :-----------: | :------: | :-----: | :-----: | :----: | :-----------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Faster R-CNN  |   R-50   | pytorch |   1x    |  52.4  |    [config](./faster-rcnn_r50_fpn_1x_ruod.py)     |        [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/faster-rcnn_r50_fpn_1x_ruod_20230420_022848-1c4a07b0.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/faster-rcnn_r50_fpn_1x_ruod_20230420_022848.log.json)        |
| Cascade R-CNN |   R-50   | pytorch |   1x    |  55.3  |    [config](./cascade-rcnn_r50_fpn_1x_ruod.py)    |       [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/cascade-rcnn_r50_fpn_1x_ruod_20230420_020450-016a540a.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/cascade-rcnn_r50_fpn_1x_ruod_20230420_020450.log.json)       |
|   RetinaNet   |   R-50   | pytorch |   1x    |  50.2  |     [config](./retinanet_r50_fpn_1x_ruod.py)      |          [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/retinanet_r50_fpn_1x_ruod_20230422_151955-557d30bb.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/retinanet_r50_fpn_1x_ruod_20230422_151955.log.json)          |
|     FCOS      |   R-50   |  caffe  |   1x    |  51.0  | [config](./fcos_r50-caffe_fpn_gn-head_1x_ruod.py) | [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/fcos_r50-caffe_fpn_gn-head_1x_ruod_20230420_024835-7bd04607.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/fcos_r50-caffe_fpn_gn-head_1x_ruod_20230420_024835.log.json) |
|     ATSS      |   R-50   | pytorch |   1x    |  55.7  |        [config](./atss_r50_fpn_1x_ruod.py)        |               [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/atss_r50_fpn_1x_ruod_20230420_014032-75749292.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/atss_r50_fpn_1x_ruod_20230420_014032.log.json)               |
|     TOOD      |   R-50   | pytorch |   1x    |  57.4  |        [config](./tood_r50_fpn_1x_ruod.py)        |               [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/tood_r50_fpn_1x_ruod_20230420_060246-0a6df011.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/tood_r50_fpn_1x_ruod_20230420_060246.log.json)               |
|    SSD300     |  VGG16   |    -    |  120e   |  46.6  |          [config](./ssd300_120e_ruod.py)          |                   [model](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/ssd300_120e_ruod_20230420_033351-076256c9.pth) \| [log](https://github.com/BIGWangYuDong/lqit/releases/download/v0.0.1rc1/ssd300_120e_ruod_20230420_033351.log.json)                   |

## Is Underwater Image Enhancement All Object Detectors Need?

TODO

## Citation

If you use `RUOD` dataset in your research, please cite it as below:

```latex
@article{fu2023rethinking,
  title={Rethinking general underwater object detection: Datasets, challenges, and solutions},
  author={Fu, Chenping and Liu, Risheng and Fan, Xin and Chen, Puyang and Fu, Hao and Yuan, Wanqi and Zhu, Ming and Luo, Zhongxuan},
  journal={Neurocomputing},
  volume={517},
  pages={243--256},
  year={2023},
  publisher={Elsevier}
}
```
