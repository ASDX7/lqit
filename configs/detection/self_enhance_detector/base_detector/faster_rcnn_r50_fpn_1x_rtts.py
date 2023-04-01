_base_ = [
    '../../_base_/models/faster-rcnn_r50_fpn.py',
    '../../_base_/datasets/rtts_coco.py',
    '../../_base_/schedules/schedule_1x.py', '../../_base_/default_runtime.py'
]

model = dict(roi_head=dict(bbox_head=dict(num_classes=5)))

# 4bs * 4GPUs
train_dataloader = dict(batch_size=4, num_workers=4)

optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001))

# show_dir = 'work_dirs/a_tienet_vis_new/rtts/faster'
#
# default_hooks = dict(
#     visualization=dict(
#         type='EnhanceDetVisualizationHook',
#         draw=True,
#         test_out_dir=show_dir + '/baseline',
#         show_on_enhance=False,
#         draw_gt=False,
#         draw_pred=True))
