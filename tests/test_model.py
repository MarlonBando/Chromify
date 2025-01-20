import torch
from model import PatchDiscriminator

def test_patch_discriminator():
    discriminator = PatchDiscriminator(3)
    dummy_input = torch.randn(16, 3, 256, 256) # batch_size, channels, size, size
    out = discriminator(dummy_input)
    assert out.shape == (16, 1, 30, 30)