import numpy as np

def Sigmoid(X):
    output = [(_Sigmoid(x))for x in X]
    return np.array(output)


def _Sigmoid(x):
    return 1 / (1 + np.exp(-x))