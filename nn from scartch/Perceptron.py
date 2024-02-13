import numpy as np

class Perceptron:
    def __init__(self,
                 learning_rate = 0.01,
                 n_iters = 1000) -> None:
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.activation_func = None
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_feature = X.shape
        self.weights = np.zerps(n_feature)
        self.bias = 0
        
        y_fit = [1 if y > 0 else 0 for _y in y]
        
        for _ in range(self.n_feature):
            for index, x in X:
                linear_output = np.dot(x, self.weights) + self.bias
                y_pred = self.activation_func(linear_output)
                
                loss = (y_fit[index] - y_pred)
                self.weights += loss * x * self.learning_rate
                self.bias += loss * self.learning_rate
    
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_pred = self.activation_func(linear_output)
        return y_pred

