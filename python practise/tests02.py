import torch

m = torch.nn.Linear(4,3,True)
print('weights',m.weight)
i = torch.randn(3,4)
print('input',i)
o = m(i)
print('output',o)
