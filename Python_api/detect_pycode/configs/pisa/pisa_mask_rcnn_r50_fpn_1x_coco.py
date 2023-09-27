_base_ = '../mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        type='PISARoIHead',
        bbox_head=dict(
            loss_bbox=dict(type='SmoothL1Loss', beta=1.0, loss_weight=1.0))))

train_cfg = dict(
    rpn_proposal=dict(
        nms_across_levels=False,
        nms_pre=2500,           #2000
        nms_post=2500,
        max_num=2500,
        nms_thr=0.7,
        min_bbox_size=0),
    rcnn=dict(
        sampler=dict(
            type='ScoreHLRSampler',
            num=1024,            #512
            pos_fraction=0.25,
            neg_pos_ub=-1,
            add_gt_as_proposals=True,
            k=0.5,
            bias=0.),
        isr=dict(k=2, bias=0),
        carl=dict(k=1, bias=0.2)))

test_cfg = dict(
    rpn=dict(
        nms_across_levels=False,
        nms_pre=2500,
        nms_post=2500,
        max_num=2500,
        nms_thr=0.7,
        min_bbox_size=0))
