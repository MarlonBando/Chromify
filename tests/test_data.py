from torch.utils.data import Dataset

from chromify.data import MyDataset


def test_my_dataset():
    """Test the MyDataset class."""
    assert True
    dataset = MyDataset("data/raw")
    assert isinstance(dataset, Dataset)
