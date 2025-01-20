import os
from data import ColorizationDataset, make_dataloaders
from src.chromify.utils import get_project_root
import math

test_data_dir = os.path.join(get_project_root(), "tests", "data", "raw")

def test_my_dataset():
    """Test the ColorizationDataset class."""
    train_colorization_dataset = ColorizationDataset(test_data_dir, split="train")
    val_colorization_dataset = ColorizationDataset(test_data_dir, split="val")

    gray_train_dir = os.path.join(test_data_dir, "train", "gray")

    assert train_colorization_dataset.path == os.path.join(test_data_dir, "train")
    assert len(train_colorization_dataset) == len(os.listdir(gray_train_dir))
    assert all(image in train_colorization_dataset.image_names for image in os.listdir(gray_train_dir))

    gray_val_dir = os.path.join(test_data_dir, "val", "gray")

    assert val_colorization_dataset.path == os.path.join(test_data_dir, "val")
    assert len(val_colorization_dataset) == len(os.listdir(gray_val_dir))
    assert all(image in val_colorization_dataset.image_names for image in os.listdir(gray_val_dir))

def test_dataloaders():
    train_colorization_dataset = ColorizationDataset(test_data_dir, split="train")
    val_colorization_dataset = ColorizationDataset(test_data_dir, split="val")

    batch_size = 16 if len(train_colorization_dataset) > 16 else len(train_colorization_dataset)

    train_dl = make_dataloaders(path=test_data_dir, batch_size=batch_size, split='train')
    val_dl = make_dataloaders(path=test_data_dir, batch_size=batch_size, split='val')

    data = next(iter(train_dl))
    Ls, abs_ = data['L'], data['ab']
    # print(Ls.shape, abs_.shape)
    # print(len(train_dl), len(val_dl))

    assert Ls.shape == (batch_size, 1, 256, 256)
    assert abs_.shape == (batch_size, 2, 256, 256)
    assert len(train_dl) == math.ceil(len(train_colorization_dataset) / batch_size) # math.ceil is because the batches cannot be floats
    assert len(val_dl) == math.ceil(len(val_colorization_dataset) / batch_size) # math.ceil is because the batches cannot be floats