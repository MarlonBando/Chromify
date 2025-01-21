import os
from datetime import datetime
from typing import Annotated

import torch
import typer
from tqdm import tqdm

from src.chromify.data import make_dataloaders
from src.chromify.model import MainModel
from src.chromify.utils import create_loss_meters, get_project_root, log_results, update_losses

app = typer.Typer()


def save_checkpoint(model, optimizer, epoch, loss, path):
    torch.save(
        {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "loss": loss,
        },
        path,
    )


def load_checkpoint(model, optimizer, path):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint["model_state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    return checkpoint["epoch"], checkpoint["loss"]


def train_model(model, data_dir, epochs, device, display_every=200):
    train_dl = make_dataloaders(path=data_dir, split="train")
    val_dl = make_dataloaders(path=data_dir, split="val")

    current_time = datetime.now()
    model_id = f"{current_time.timetuple().tm_yday:03d}" f"{current_time.hour:02d}" f"{current_time.minute:02d}"

    best_val_loss = float("inf")
    # Patience in training refers to how many epochs
    # to wait before stopping when a monitored metric stops improving.
    # Used with Early Stopping to prevent overfitting
    patience = 10
    patience_counter = 0
    models_dir = os.path.join(get_project_root(), "models")
    os.makedirs(models_dir, exist_ok=True)

    for e in range(epochs):
        # Training phase
        model.train()
        train_loss_meter_dict = create_loss_meters()
        for i, data in enumerate(tqdm(train_dl)):
            model.setup_input(data)
            model.optimize()
            update_losses(model, train_loss_meter_dict, count=data["L"].size(0))

            if i % display_every == 0:
                print(f"\nEpoch {e + 1} / {epochs}")
                print(f"Iteration {i} / {len(train_dl)}")
                log_results(train_loss_meter_dict)

        # Validation phase
        model.eval()
        val_loss_meter_dict = create_loss_meters()
        with torch.no_grad():
            for data in val_dl:
                model.setup_input(data)
                model.forward()
                update_losses(model, val_loss_meter_dict, count=data["L"].size(0))

        current_val_loss = sum(meter.avg for meter in val_loss_meter_dict.values())

        # If we see that after multiple epochs the loss is not improving
        # we stop to save resources.
        if current_val_loss < best_val_loss:
            best_val_loss = current_val_loss
            save_checkpoint(
                model, model.optimizer_G, e, current_val_loss, os.path.join(models_dir, f"{model_id}_{e}.pth")
            )
            patience_counter = 0
        else:
            patience_counter += 1

        # Early stopping
        if patience_counter >= patience:
            print(f"Early stopping triggered after {e + 1} epochs")
            break


@app.command()
def train(epochs: Annotated[int, typer.Option("--epochs", "-e")] = 10):
    # Define the device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Define the model
    model = MainModel()
    model = model.to(device)

    data_dir = os.path.join(get_project_root(), "data", "raw")

    train_model(model, data_dir, epochs, device)


if __name__ == "__main__":
    app()
