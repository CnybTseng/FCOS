# Author    : Zeng Zhiwei
# Date      : 2020/1/21

from collections import namedtuple

StageSpec = namedtuple('StageSpec', ['index', 'block_count', 'return_features'])

ResNet50FPNStage2345 = tuple(
    StageSpec(index=i, block_count=b, return_features=r)
    for (i,b,r) in ((1,3,True), (2,4,True), (3,6,True), (4,3,True))
)

