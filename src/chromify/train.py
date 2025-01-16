import os
import sys
import torch
import torch.nn as nn
from model import UNetEfficientNetV2
import torchvision.transforms as transforms
from data import MyDataset

sys.path.insert(0, os.path.abspath('.'))

# Define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define the model, loss function, and optimizer
model = UNetEfficientNetV2() # it has default values UNetEfficientNetV2(encoder_name='tf_efficientnetv2_s', pretrained=True)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# data loader paths
train_dir = "./data/raw/train/"
# train_grayscale_dir = "./data/raw/train/gray"
# train_color_dir = "./data/raw/train/color"

val_dir = "./data/raw/val/"
# val_grayscale_dir = "./data/raw/val/gray"
# val_color_dir = "./data/raw/val/color"

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
])

train_dataset = MyDataset(train_dir, transform=transform)
val_dataset = MyDataset(val_dir, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=16, shuffle=False)

def train(epochs: int = 10):
    for epoch in range(epochs):
        model.train()
        train_loss = 0.0
        for L, AB in train_loader:
            L, AB = L.to(device), AB.to(device)

            optimizer.zero_grad()
            outputs = model(L)  # Predict AB channels
            loss = criterion(outputs, AB)  # Compute loss
            loss.backward()  # Backpropagation
            optimizer.step()  # Update weights

            train_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for L, AB in val_loader:
                L, AB = L.to(device), AB.to(device)
                outputs = model(L)
                loss = criterion(outputs, AB)
                val_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs}, Train Loss: {train_loss / len(train_loader):.4f}, Val Loss: {val_loss / len(val_loader):.4f}")

train()