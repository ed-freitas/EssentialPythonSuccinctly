# Importing PyTorch
import torch
import torch.nn as nn
import torch.optim as optim

# Sample data
X_train = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y_train = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

# Define the model
class XORModel(nn.Module):
    def __init__(self):
        super(XORModel, self).__init__()
        self.layer1 = nn.Linear(2, 8)
        self.layer2 = nn.Linear(8, 1)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.sigmoid(self.layer2(x))
        return x

# Instantiate the model, define loss function and optimizer
model = XORModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    optimizer.zero_grad()  # Reset gradients
    output = model(X_train)  # Forward pass
    loss = criterion(output, y_train)  # Compute loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights

# Make predictions
with torch.no_grad():
    predictions = model(X_train)
    print("Predictions:\n", predictions)