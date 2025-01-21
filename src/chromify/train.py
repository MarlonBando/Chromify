import os

import torch
from src.chromify.model import MainModel
from tqdm import tqdm
import typer
from typing import Annotated
from src.chromify.utils import create_loss_meters, get_project_root, log_results, update_losses
from pytorch_lightning import Trainer, ModelCheckpoint, EarlyStopping
from src.chromify.data import make_dataloaders

app = typer.Typer()

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

@app.command()
def train(epochs: Annotated[int, typer.Option("--epochs", "-e")] = 10):
    print(os.path.join(get_project_root(), "models"))
    # Define the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Define the model
    model = MainModel()

    models_dir = os.path.join(get_project_root(), "models")
    checkpoint_callback = ModelCheckpoint(dirpath=models_dir, monitor="val_loss", mode="min")
    early_stopping_callback = EarlyStopping(monitor="val_loss", patience=10, verbose=True, mode="min")
    trainer = Trainer(callbacks=[checkpoint_callback, early_stopping_callback])
    trainer.fit(model)

    model = model.to(device)

    data_dir = os.path.join(get_project_root(), "data", "raw")
    
    train_model(model, data_dir, epochs)

if __name__ == "__main__":
    app()