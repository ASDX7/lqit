_base_ = '../0_raw_image_detectors/faster-rcnn_r50_fpn_2x_urpc-coco.py'

train_dataloader = dict(
    dataset=dict(data_prefix=dict(img='13_uwdet_UIEC2Net/')))
val_dataloader = dict(dataset=dict(data_prefix=dict(img='13_uwdet_UIEC2Net/')))
test_dataloader = val_dataloader