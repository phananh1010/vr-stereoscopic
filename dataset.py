import torch as tc
import torchvision as tv
from PIL import Image
import numpy as np
import glob

class StereoReader(tc.utils.data.Dataset):
    
    def __init__(self, filepath, transform):
        #TODO: read all file in the given folder
        self.filepath_dict, self.vid_filepath_list, self.frame_filepath_list = self.extract_file_hierachy(filepath)
        self.transform = transform
        return
    
    def __len__(self):
        return len(self.frame_filepath_list)/2
    
    def __getitem__(self, idx):
        frame_filepath_left, frame_filepath_right = self.frame_filepath_list[idx*2], self.frame_filepath_list[idx*2+1], 
        img_left, img_right = self.read_image(frame_filepath)
        return img_left, img_right
    
    #### FUNCTION to initialize file structure from dataset directory
    def explore_directory(self, filepath):
        #TODO: given a filepath: return list of file/dir which is direct child of the input
        filepath_list = glob.glob(filepath + '/*')
        file_list = [item.split('/')[-1] for item in filepath_list]
        return filepath_list, file_list
    
    def extract_file_hierachy(self, filepath):
        #TODO: for the root filepath, extract list of videos, and the frames for each video
        #INPUT: root dir path
        #OUTPUT: python directory storing the result with key is the filename & vidname, list of all vid, list of all file
        result = {}
        frame_filepath_list_total = []
        vid_filepath_list, vid_filename_list = self.explore_directory(filepath)
        for idx, vid_filepath in enumerate(vid_filepath_list):
            vid_filename = vid_filename_list[idx]
            frame_filepath_list, frame_filename_list = self.explore_directory(vid_filepath)
            frame_filename_list = sorted(frame_filename_list) #sorted, to get left right easily
            result[vid_filename] = frame_filepath_list
            frame_filepath_list_total += frame_filepath_list
        return result, vid_filepath_list, frame_filepath_list_total
    
    ##### Functions to read & process image
    def read_image(self, frame_filepath):
        return self.transform(Image.open(frame_filepath))
    
