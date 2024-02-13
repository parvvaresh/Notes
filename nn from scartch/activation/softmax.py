import numpy as np


def softmax(X):
  return (np.exp(X)) / sum(np.exp(X))