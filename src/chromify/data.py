from pathlib import Path
import glob
import kagglehub
import typer
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
import torch
import os

train_path : str = "~/.cache/kagglehub/datasets/seungjunleeofficial/image-colorization/versions/1/train"
test_path : str = "~/.cache/kagglehub/datasets/seungjunleeofficial/image-colorization/versions/1/val"

class MyDataset(Dataset):
    """My custom dataset."""
    train_dataset = sorted(glob.glob(f"{train_path}/gray/*.jpg"))
    target_dataset = sorted(glob.glob(f"{train_path}/color/*.jpg"))
    test_dataset = sorted(glob.glob(f"{test_path}/gray/*.jpg"))
    test_target = sorted(glob.glob(f"{test_path}//color/*.jpg"))
    
    train_dataset = [torch.from_numpy(plt.imread(img)) for img in train_dataset]
    target_dataset = [torch.from_numpy(plt.imread(img)) for img in target_dataset]
    test_dataset = [torch.from_numpy(plt.imread(img)) for img in test_dataset]
    test_target = [torch.from_numpy(plt.imread(img)) for img in test_target]
    def __init__(self, raw_data_path: Path) -> None:
        self.data_path = raw_data_path

    def __len__(self) -> int:
        """Return the length of the dataset."""

    def __getitem__(self, index: int):
        """Return a given sample from the dataset."""
        try:
            img = torch.from_numpy(plt.imread(self.data_path[index]))
            return img
        except Exception as e:
            print(f"Error reading image {self.data_path[index]}")
            print(e)
            return None

    def preprocess(self, raw_data_path: Path, output_folder: Path) -> None:
        """Preprocess the raw data and save it to the output folder."""        
        train_dataset = torch.cat(train_dataset)
        target_dataset = torch.cat(target_dataset)
        test_dataset = torch.cat(test_dataset)
        test_target = torch.cat(test_target)
        
        train_dataset = train_dataset.unsqueeze(1).float()
        target_dataset = target_dataset.unsqueeze(1).float()
        test_dataset = test_dataset.unsqueeze(1).float()
        test_target = test_target.unsqueeze(1).float()
        
        torch.save(train_dataset, f"{output_folder}/train_train.pt")
        torch.save(target_dataset, f"{output_folder}/target_train.pt")
        torch.save(test_dataset, f"{output_folder}/train_train.pt")
        torch.save(test_target, f"{output_folder}/target_train.pt")
        


def preprocess(raw_data_path: Path, output_folder: Path) -> None:
    print("Preprocessing data...")
    dataset = MyDataset(raw_data_path)
    dataset.preprocess(output_folder)


def get_raw_data():
    path = kagglehub.dataset_download(handle = "seungjunleeofficial/image-colorization")
    print("Path to dataset files:", path)


if __name__ == "__main__":
    typer.run(preprocess)
