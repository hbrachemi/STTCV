import slidingwindow as sw
import numpy as np
import torch
import math
from torch.utils.data import random_split


def patch_selection(img,patch_size=16,num_patches=196):
  assert pow(num_patches,0.5) == int(pow(num_patches,0.5)), 'destination image must be square: Please chose a patch number = NÃ‚Â²'
 
  img=np.rot90(img)
  windows = sw.generate(img, sw.DimOrder.HeightWidthChannel,patch_size,0)
 
  q=int(len(windows)/num_patches)
  if q==0:
    return np.rot90(img,3)
  y=np.empty((int(pow(num_patches,0.5))*patch_size,int(pow(num_patches,0.5))*patch_size,3))
  
  i=0
  j=0

  for k,window in enumerate(windows):    
    if k % q == 0:
      
      subset = img[window.indices()]
      subset=np.rot90(subset,3)
      
      if i >= int(pow(num_patches,0.5)):
        i=0
        j+=1
      if j < int(pow(num_patches,0.5)):
        y[(slice(j*patch_size,(j+1)*patch_size, None), slice(i*patch_size,(i+1)*patch_size, None))]=subset
        i+=1
  return y
  
  
class ToTensor(object):
    """Convert ndarrays in sample to Tensors."""

    def __call__(self, sample):
        video, label = sample
        video=torch.from_numpy(video)
        return video,label
        
        
        
class Normalize(object):
    """Normalize tensors."""
    def __init__(self, mean, std):
      self.mean=mean
      self.std=std
    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        for i in range(3):
         image[i,:,:]=(image[i,:,:]-self.mean[i])/self.std[i] 
        return  image, label
        
        
def center_crop(size, image):
    """
    Perform center crop on input images.
    Args:
        size (int): size of the cropped height and width.
        image (array): the image to perform center crop.
    """
    height = image.shape[0]
    width = image.shape[1]
    y_offset = int(math.ceil((height - size) / 2))
    x_offset = int(math.ceil((width - size) / 2))
    cropped = image[y_offset : y_offset + size, x_offset : x_offset + size, :]
    assert cropped.shape[0] == size, "Image height not cropped properly"
    assert cropped.shape[1] == size, "Image width not cropped properly"
    return cropped