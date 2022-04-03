import torch as tc
import torchvision as tv

import numpy as np
import glob

class StereoReader(tc.utils.data.Dataset):
    
    def __init__(self, ):
        
    
    def __len__(self):
        return len(self.tilename_list)
    
    def __getitem__(self, idx):
        self.check_internal_consistency()
        vid_idx, seg_idx, tile_idx = self.get_indices(idx)
        tilepath = self.dat[vid_idx][seg_idx][tile_idx]
        result = {self.KEY_FILEPATH: tilepath, 
                  self.KEY_IDX: idx, 
                  self.KEY_VIDIDX: vid_idx, 
                  self.KEY_SEGIDX: seg_idx,
                  self.KEY_TILEIDX: tile_idx}
        result = {**result, **self.parse_info(tilepath)}
        return result