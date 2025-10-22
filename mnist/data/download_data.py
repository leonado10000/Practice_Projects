from torchvision import datasets

train_dataset = datasets.MNIST(root='data/', train=True, transform=None, download=True)
test_dataset = datasets.MNIST(root='data/', train=False, transform=None, download=True)