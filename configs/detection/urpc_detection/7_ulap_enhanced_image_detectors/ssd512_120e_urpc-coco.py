_base_ = '../0_raw_image_detectors/ssd512_120e_urpc-coco.py'

train_dataloader = dict(
    dataset=dict(dataset=dict(data_prefix=dict(img='7_uwdet_ULAP/'))))
val_dataloader = dict(dataset=dict(data_prefix=dict(img='7_uwdet_ULAP/')))
test_dataloader = val_dataloader
