softmax function is used to change the range of a distribution from [x,y] to [0,1].

softmax(Xi) = e^xi / sum( j:e^xj)

example
[8,5,0]

e^8 = 2981.0
e^5 = 148.4 
e^0 = 1.0

sum( j:e^xj) = e^8 + e^5 + e^0 = 3130.4

softmax(8) = 2981.0/3130.4 = 0.9523
softmax(5) = 148.0/3130.4 = 0.0474
softmax(0) = 1.0/3130.4 = 0.0003


