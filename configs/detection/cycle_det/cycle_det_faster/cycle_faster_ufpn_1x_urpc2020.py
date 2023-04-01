_base_ = '../base_detector/faster_rcnn_r50_fpn_1x_urpc2020.py'

# model settings
model = dict(
    type='CycleTwoStageWithEnhanceHead',
    loss_weight=[0.5, 0.5],
    neck=dict(type='UFPN'),
    enhance_head=dict(
        _scope_='lqit',
        type='CycleEnhanceHead',
        in_channels=256,
        upscale_factor=4,
        num_convs=2,
        gt_preprocessor=dict(
            type='GTPixelPreprocessor',
            mean=[123.675, 116.28, 103.53],
            std=[58.395, 57.12, 57.375],
            bgr_to_rgb=True,
            pad_size_divisor=32,
            element_name='img'),
        spacial_loss=dict(type='SpatialLoss', loss_weight=1.0),
        tv_loss=dict(type='MaskedTVLoss', loss_mode='mse', loss_weight=10.0),
        structure_loss=dict(
            type='StructureFFTLoss',
            radius=4,
            pass_type='high',
            channel_mean=True,
            loss_type='mse',
            guid_filter=dict(
                type='GuidedFilter2d', radius=32, eps=1e-4, fast_s=2),
            loss_weight=0.1)))

# dataset settings
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='lqit.SetInputImageAsGT'),
    dict(type='lqit.PackInputs')
]
train_dataloader = dict(dataset=dict(pipeline=train_pipeline))