import torch
import torch.nn as nn


X = torch.randn(3,2)
model = nn.Linear(2,1)
y_pred = model(X)

print(model.weight, y_pred.shape)