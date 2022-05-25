import os
import torch
import numpy as np
import cv2
from torchvision import datasets, transforms
from torch.utils.data import Dataset
import pickle
from tools import *

p=625

class dataset(Dataset):
    """Adaptive dataset."""

    def __init__(self,labels_path='../Databases/scores.pickle' ,db_path='./',q=None,
                 ids_path='../Databases/IDs.pickle',part='', transform=None):
        """
        Args:
            labels_path (string): Path to the pickle file dictionnary.
            db_path (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        
        self.labels_path=labels_path
        self.db_path=db_path
        self.ids_path=ids_path
        self.part=part
        self.transform=transform
        
        self.ids_path=self.ids_path.replace('.pickle','')
        self.ids_path=self.ids_path+"_"+str(part)+".pickle"
        pickle_in = open(self.ids_path,'rb')
        self.list_IDs= pickle.load(pickle_in)
        self.list_IDs=list(self.list_IDs)
        pickle_in.close()

        pickle_in = open(self.labels_path,'rb')
        self.labels = pickle.load(pickle_in)
        pickle_in.close()
        
        self.q=q
        
    def __len__(self):
        return int(len(self.list_IDs))

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        video_name = os.path.join(self.db_path,
                                self.list_IDs[idx])
        
        images=[]
        vidcap = cv2.VideoCapture(video_name)
        success,image = vidcap.read()
        count=0
        while success:
          images.append(image)
          count += 1
          success,image = vidcap.read()
        if count == 0:
          print("Invalid video")
        if self.q is not None:
          c=int(count/self.q)
          X=[]
          for i in range(self.q):
           
            resized = patch_selection(images[i*c],16,p)
            resized=np.asarray(resized)
            X.append(resized)
          X=np.array(X)
          video=torch.from_numpy(X)
          video = (video.permute(3,0,1,2)).float()

        label = self.labels[self.list_IDs[idx]]
        label = np.array([label])
        label = label.astype('float32')

        return video,label