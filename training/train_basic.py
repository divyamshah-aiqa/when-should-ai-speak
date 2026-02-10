import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader

# Dataset class
class MyDataset(Dataset):
    def __init__(self, data_file):
        # TODO: load CSV, tokenize text, map labels
        pass
    def __len__(self):
        # TODO: return dataset length
        pass
    def __getitem__(self, idx):
        # TODO: return one sample (features, label)
        pass

# Simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        # TODO: define layers
    def forward(self, x):
        # TODO: forward pass
        pass

def train():
    # TODO: load dataset
    # TODO: initialize model, loss, optimizer
    # TODO: loop over epochs
    #   - forward pass
    #   - compute loss
    #   - backward pass
    #   - optimizer step
    # TODO: print accuracy/loss per epoch

if __name__ == "__main__":
    train()
