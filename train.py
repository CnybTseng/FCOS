# Author    : Zeng Zhiwei
# Date      : 2020/1/21

import torch
import argparse
from core.config import cfg

def main():
    parser = argparse.ArgumentParser(description="FCOS object detector training")
    parser.add_argument("--config-file", default="", metavar="FILE", help="path to config file", type=str)
    parser.add_argument("opts", default=None, help="modify config options using the command line", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    print(cfg)

if __name__ == '__main__':
    main()