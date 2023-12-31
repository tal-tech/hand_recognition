_base_ = '../mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py'

conv_cfg = dict(type='ConvWS')
norm_cfg = dict(type='GN', num_groups=32, requires_grad=True)
model = dict(
    pretrained='open-mmlab://jhu/resnet50_gn_ws',
    #pretrained='~/.cache/torch/checkpoints/resnet50_gn_ws-15beedd8.pth',
    backbone=dict(conv_cfg=conv_cfg, norm_cfg=norm_cfg),
    neck=dict(conv_cfg=conv_cfg, norm_cfg=norm_cfg),
    roi_head=dict(
        bbox_head=dict(
            type='Shared4Conv1FCBBoxHead',
            conv_out_channels=256,
            conv_cfg=conv_cfg,
            norm_cfg=norm_cfg),
        mask_head=dict(conv_cfg=conv_cfg, norm_cfg=norm_cfg)))
# learning policy
# lr_config = dict(step=[16, 22])
# total_epochs = 24
lr_config = dict(step=[28, 34])
total_epochs = 36
