from PIL import Image
import torch
import numpy as np
from skimage.color import lab2rgb

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def test_model(grayscale_img_path, model, transform):
    grayscale_img = Image.open(grayscale_img_path).convert("L")
    input_tensor = transform(grayscale_img).unsqueeze(0).to(device)  # Add batch dimension

    # Predict AB channels
    model.eval()
    with torch.no_grad():
        pred_ab = model(input_tensor).cpu().squeeze(0).numpy()

    # Combine L and AB
    input_l = input_tensor.cpu().squeeze(0).numpy()
    lab_img = np.concatenate([input_l.transpose(1, 2, 0), pred_ab.transpose(1, 2, 0)], axis=-1)

    # Convert LAB to RGB
    rgb_result = lab2rgb(lab_img)
    return rgb_result
