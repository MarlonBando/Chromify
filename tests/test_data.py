import os
import sys
from chromify.data import ColorizationDataset, make_dataloaders
import math

# sys.path.insert(0, os.path.abspath('..'))

def test_my_dataset():
    """Test the ColorizationDataset class."""
    colorizationDataset = ColorizationDataset("./data/raw", split="train")

    assert colorizationDataset.path == "./data/raw/train"
    assert len(colorizationDataset) == len(os.listdir("./data/raw/train/gray"))
    assert "000000000009.jpg" in colorizationDataset.image_names

def test_dataloaders():
    train_colorizationDataset = ColorizationDataset("./data/raw", split="train")
    val_colorizationDataset = ColorizationDataset("./data/raw", split="val")

    data_dir = "./data/raw/"
    batch_size = 16

    train_dl = make_dataloaders(path=data_dir, batch_size=batch_size, split='train')
    val_dl = make_dataloaders(path=data_dir, batch_size=batch_size, split='val')

    data = next(iter(train_dl))
    Ls, abs_ = data['L'], data['ab']
    # print(Ls.shape, abs_.shape)
    # print(len(train_dl), len(val_dl))

    assert Ls.shape == (batch_size, 1, 256, 256)
    assert abs_.shape == (batch_size, 2, 256, 256)
    assert len(train_dl) == math.ceil(len(train_colorizationDataset) / batch_size) # math.ceil is because the batches cannot be floats
    assert len(val_dl) == math.ceil(len(val_colorizationDataset) / batch_size) # math.ceil is because the batches cannot be floats