import os

import torch
from src.chromify.model import MainModel
from tqdm import tqdm
import argparse
from src.chromify.utils import create_loss_meters, get_project_root, log_results, update_losses
from src.chromify.data import make_dataloaders

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Train the model")
    parser.add_argument(
        "epochs", type=int, nargs="?", default=10, help="Number of epochs to train the model"
    )
    return parser.parse_args()

def train_model(model, data_dir, epochs, display_every=200):
    train_dl = make_dataloaders(path=data_dir, split="train")
    val_dl = make_dataloaders(path=data_dir, split="val")

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
                print(f"\nEpoch {e + 1} / {epochs}")
                print(f"Iteration {i} / {len(train_dl)}")
                log_results(loss_meter_dict)  # function to print out the losses
                # visualize(model, data, save=False) # function displaying the model's outputs

def main():
    args = parse_args()

    # Define the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Define the model, loss function, and optimizer
    model = MainModel()
    model = model.to(device)

    data_dir = os.path.join(get_project_root(), "data", "raw")
    
    train_model(model, data_dir, epochs=args.epochs)

if __name__ == "__main__":
    main()