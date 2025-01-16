import os
import sys

sys.path.insert(0, os.path.abspath('.'))
# print(sys.path)
import src.chromify.data as data


def test_my_dataset():
    """Test the MyDataset class."""
    MyDataset = data.MyDataset("./data/raw/train")

    assert MyDataset.data_path == "./data/raw/train"
    assert MyDataset.grayscale_dir == "./data/raw/train/gray"
    assert MyDataset.color_dir == "./data/raw/train/color"
    assert len(MyDataset) == len(os.listdir("./data/raw/train/gray"))
