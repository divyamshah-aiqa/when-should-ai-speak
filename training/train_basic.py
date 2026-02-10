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
    # Step 1: Load dataset
    dataset = MyDataset("training/data.csv")
    dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

    # Step 2: Initialize model, loss, optimizer
    model = SimpleModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Step 3: Training loop
    for epoch in range(5):  # 5 epochs
        total_loss = 0
        correct = 0
        total = 0

        for texts, labels in dataloader:
            # For now, fake token IDs (we’ll fix later)
            inputs = torch.randint(0, 1000, (len(labels), 10))
            labels = torch.tensor(labels)

            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

        print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}, Accuracy: {correct/total:.2f}")
