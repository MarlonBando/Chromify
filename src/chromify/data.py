import os
from pathlib import Path
from PIL import Image

import kagglehub
import typer
import torch
from torch.utils.data import Dataset
from skimage.color import rgb2lab

class MyDataset(Dataset):
    """My custom dataset."""

    def __init__(self, raw_data_path: Path, transform=None) -> None:
        """
        Args:
            grayscale_dir (str): Path to grayscale images (L-mode).
            color_dir (str): Path to RGB color images.
        """
        self.data_path = raw_data_path
        self.grayscale_dir = os.path.join(self.data_path, "gray")
        self.color_dir = os.path.join(self.data_path, "color")
        self.image_names = os.listdir(self.grayscale_dir)  # Assumes matching filenames in both directories
        self.transform = transform

    def __len__(self) -> int:
        """Return the length of the dataset."""        
        return len(self.image_names)

    def __getitem__(self, index: int):
        """Return a given sample from the dataset."""
        grayscale_path = os.path.join(self.grayscale_dir, self.image_names[index])
        color_path = os.path.join(self.color_dir, self.image_names[index])

        # Load images
        grayscale_img = Image.open(grayscale_path).convert("L")
        color_img = Image.open(color_path).convert("RGB")

        if self.transform:
            # Apply transform to both grayscale and color images
            grayscale_img = self.transform(grayscale_img)
            color_img = self.transform(color_img)

        # Convert color image to LAB
        color_lab = rgb2lab(color_img.permute(1, 2, 0).numpy() / 255.0)  # Convert RGB → LAB
        color_lab = torch.tensor(color_lab, dtype=torch.float32).permute(2, 0, 1)  # HWC → CHW

        # Split LAB into L and AB
        L = grayscale_img  # Grayscale (L-mode)
        AB = color_lab[1:] / 128.0  # Normalize AB channels to [-1, 1]

        return L, AB


def preprocess(raw_data_path: Path, output_folder: Path) -> None:
    print("Preprocessing data...")
    dataset = MyDataset(raw_data_path)
    dataset.preprocess(output_folder)


def get_raw_data():
    path = kagglehub.dataset_download("seungjunleeofficial/image-colorization")
    print("Path to dataset files:", path)


if __name__ == "__main__":
    typer.run(preprocess)
