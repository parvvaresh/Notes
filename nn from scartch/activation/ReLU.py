import numpy as np

def ReLU(X):
   X = np.array(X) # for check array
   return np.where(X > 0, X, 0) 
    