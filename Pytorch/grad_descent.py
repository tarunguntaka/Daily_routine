import torch
import numpy as np

X = np.array([1,2,3,4,5], dtype = float32)
Y = np.array([2,4,6,8,10], dtype = float32)

# function 

#weights
w = np.zeros(5)


def f(x):
    return w*x

def loss(y, y_pred):
    return ((y_pred-y)**2).mean()

# l = 1/N *(w.x-y_pred)**2 
#dl/dw  = 1/N * 2 (w*x-y_pred)*x

def gradient(x,y,y_pred):
    return  2 *np.dot(2*x, y-y_pred).mean()


lr = 0.01 
n_iters = 10 


for epoch in range(n_iters):

    Y_pred = f(X)

    l = loss(Y,Y_pred)

    w-= lr*gradient(X,Y,Y_pred)

    print(f' epoch = {epoch+1}, loss = {l:.8f}, weights = {w:.3f}')
    print(f' pred after training {f(10):.3f}')








