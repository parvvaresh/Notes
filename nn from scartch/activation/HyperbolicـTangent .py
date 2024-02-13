import numpy as np



def Hyperbolic_Tangent(X):
    output = [_Hyperbolic_Tangent(x) for x in X]
    return np.array(output)

def _Hyperbolic_Tangent(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)) 