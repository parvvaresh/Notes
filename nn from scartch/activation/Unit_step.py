import numpy as np

def unit_step(X):
   X = np.array(X) # for check array
   return np.where(X > 0, 1, 0) 
