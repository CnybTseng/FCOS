# Author    : Zeng Zhiwei
# Date      : 2020/1/21

from yacs.config import CfgNode as CN

_C = CN()

# ----------------------------------------------------------------------------
# Dataset
# ----------------------------------------------------------------------------
_C.DATASET = CN()
_C.DATASET.TRAIN = ()
_C.DATASET.TEST = ()

# ----------------------------------------------------------------------------
# Dataloader
# ----------------------------------------------------------------------------
_C.DATALOADER = CN()
_C.DATALOADER.NUM_WORKERS = 4

# ----------------------------------------------------------------------------
# Solver
# ----------------------------------------------------------------------------
_C.SOLVER = CN()
_C.SOLVER.MAX_ITER = 10000
_C.SOLVER.WARMUP = 1000
_C.SOLVER.BASE_LR = 0.001
_C.SOLVER.LR_GAMMA = 0.1
_C.SOLVER.MILESTONES = (8000,9000)
_C.SOLVER.MOMENTUM = 0.9
_C.SOLVER.WEIGHT_DECAY = 0.0005
_C.SOLVER.BATCH_SIZE = 8