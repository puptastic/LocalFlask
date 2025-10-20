import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plt
from essential_functions import timing

@timing
def mini_batching(size):
    # Load data
    wine = load_wine()
    X = torch.tensor(wine.data, dtype=torch.float32)
    y = torch.tensor(wine.target, dtype=torch.long)

    # DataLoader call
    batch_size = size
    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Create model with two hidden layers
    model = nn.Sequential(
        nn.Linear(13, 10),
        nn.ReLU(),
        nn.Linear(10, 10),
        nn.ReLU(),
        nn.Linear(10, 3)
    )

    # Define criterion and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Best loss and checkpoint
    best_loss = float('inf')
    checkpoint_path = "best_model.pth"

    # model training via mini-batching
    num_epochs = 50
    epoch_losses = {'loss': []}
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for batch_X, batch_y in dataloader:
            optimizer.zero_grad()
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            # print(f"Batch loss: {loss.item():.4f}")
            running_loss += loss.item() * batch_X.size(0)

        epoch_loss = running_loss / len(dataloader.dataset)
        epoch_losses['loss'].append(epoch_loss)
        # print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {epoch_loss:.4f}")

        if epoch_loss < best_loss:
            best_loss = epoch_loss
            torch.save(model, checkpoint_path)


    # Plotting data
    epochs = range(1, num_epochs + 1)
    epoch_loss = epoch_losses['loss']
    # print(epoch_loss)

    plt.figure(figsize = (10,10))
    plt.plot(epochs, epoch_loss, label = 'Average Loss', color = 'blue', marker='o')
    plt.title('Batch Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Average Loss')
    plt.legend()
    plt.show()


mini_batching(16)