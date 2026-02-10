import torch
from torch import nn, optim
from torch.utils.data import Dataset, DataLoader
import pandas as pd


class MyDataset(Dataset):
    def __init__(self, data_file):
        # Load CSV
        df = pd.read_csv(data_file)
        self.texts = df['text'].tolist()
        self.labels = df['label'].map({'clear':0, 'ambiguous':1}).tolist()

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        # For now, just return raw text + label
        return text, label


class SimpleModel(nn.Module):
    def __init__(self, vocab_size=1000, embed_dim=16, hidden_dim=32, num_classes=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc1 = nn.Linear(embed_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        # x will be token IDs
        x = self.embedding(x)
        x = x.mean(dim=1)  # average embeddings
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


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
