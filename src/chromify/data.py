import os
from pathlib import Path
from PIL import Image

import kagglehub
import typer
import torch
from torchvision import transforms
import numpy as np
from torch.utils.data import Dataset, DataLoader
from skimage.color import rgb2lab

SIZE = 256
class ColorizationDataset(Dataset):
    def __init__(self, path, split='train'):
        if split == 'train':
            self.transforms = transforms.Compose([
                transforms.Resize((SIZE, SIZE),  Image.BICUBIC),
                transforms.RandomHorizontalFlip(), # A little data augmentation!
            ])
        elif split == 'val':
            self.transforms = transforms.Resize((SIZE, SIZE),  Image.BICUBIC)
        
        self.split = split
        self.size = SIZE
        self.path = os.path.join(path, self.split)
        self.image_names = os.listdir(os.path.join(self.path, "gray"))  # Assumes matching filenames in both directories

    def __getitem__(self, idx):
        gray_path = os.path.join(self.path, "gray", self.image_names[idx])
        color_path = os.path.join(self.path, "color", self.image_names[idx])

        gray_img = Image.open(gray_path).convert("L")
        gray_img = self.transforms(gray_img)
        gray_img = np.array(gray_img)
        gray_img = gray_img.astype("float32") # Converting RGB to L*a*b
        gray_img = transforms.ToTensor()(gray_img)

        color_img = Image.open(color_path).convert("RGB")
        color_img = self.transforms(color_img)
        color_img = np.array(color_img)
        color_img_lab = rgb2lab(color_img).astype("float32") # Converting RGB to L*a*b
        color_img_lab = transforms.ToTensor()(color_img_lab)

        L = gray_img[[0], ...] / 50. - 1. # Between -1 and 1
        ab = color_img_lab[[1, 2], ...] / 110. # Between -1 and 1
        
        return {'L': L, 'ab': ab}
    
    def __len__(self):
        return len(self.image_names)

def make_dataloaders(batch_size=16, n_workers=4, pin_memory=True, **kwargs): # A handy function to make our dataloaders
    dataset = ColorizationDataset(**kwargs)
    dataloader = DataLoader(dataset, batch_size=batch_size, num_workers=n_workers,
                            pin_memory=pin_memory)
    return dataloader

# if __name__ == "__main__":
    # typer.run(preprocess)
