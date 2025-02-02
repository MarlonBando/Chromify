import os
import torch
import numpy as np
import src.chromify.utils as utils

def test_get_project_root():
    assert os.path.exists(utils.get_project_root())
    assert os.path.basename(utils.get_project_root()) in ["Chromify", "chromify"]
    assert os.path.isdir(os.path.join(utils.get_project_root(), "data"))
    assert os.path.isdir(os.path.join(utils.get_project_root(), "tests"))
    assert os.path.isdir(os.path.join(utils.get_project_root(), "src"))

def test_lab_to_rgb():
    L = torch.randn(1, 1, 256, 256)
    ab = torch.randn(1, 2, 256, 256)
    rgb_imgs = utils.lab_to_rgb(L, ab)
    assert rgb_imgs.shape == (1, 256, 256, 3)
    assert rgb_imgs.dtype == np.float32