_base_ = 'urpc_faster_base.py'

model = dict(
    enhance_model=dict(generator=dict(model=dict(kernel_size=[3, 3, 3]))))