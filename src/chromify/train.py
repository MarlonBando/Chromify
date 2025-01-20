import os
import sys

import torch
import torch.nn as nn
from model import MainModel
from tqdm import tqdm
from src.chromify.utils import create_loss_meters, get_project_root, log_results, update_losses

from data import make_dataloaders

sys.path.insert(0, os.path.abspath("."))

# Define the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the model, loss function, and optimizer
model = MainModel()
model = model.to(device)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

data_dir = os.path.join(get_project_root(), "data", "raw")

train_dl = make_dataloaders(path=data_dir, split="train")
val_dl = make_dataloaders(path=data_dir, split="val")


def train_model(model, train_dl, epochs, display_every=200):
    data = next(iter(val_dl))  # getting a batch for visualizing the model output after fixed intrvals
    for e in range(epochs):
        loss_meter_dict = create_loss_meters()  # function returing a dictionary of objects to
        i = 0  # log the losses of the complete network
        for data in tqdm(train_dl):
            model.setup_input(data)
            model.optimize()
            update_losses(model, loss_meter_dict, count=data["L"].size(0))  # function updating the log objects
            i += 1
            if i % display_every == 0:
                print(f"\nEpoch {e+1}/{epochs}")
                print(f"Iteration {i}/{len(train_dl)}")
                log_results(loss_meter_dict)  # function to print out the losses
                # visualize(model, data, save=False) # function displaying the model's outputs


model = MainModel()

if __name__ == "__main__":
    train_model(model, train_dl, 10)
