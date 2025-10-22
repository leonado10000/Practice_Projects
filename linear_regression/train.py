import torch
from torch.nn import MSELoss
from torch.optim import SGD
import pandas as pd
from model import LR
print("Hello, Non Linears!")

print("\n\n")
X = torch.from_numpy(pd.read_csv('X.csv').values).float()
y = torch.from_numpy(pd.read_csv('y.csv').values).float()

model = LR(input_dim=X.shape[1], output_dim=y.shape[1])
mse = MSELoss()
sgd = SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    y_pred = model(X)
    loss = mse(y_pred, y)
    loss.backward()
    sgd.step()
    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

print("\n\n")
