import torch

if torch.cuda.is_available() :
    print(f"Using device: ",torch.cuda)

print(torch.cuda.__all__)