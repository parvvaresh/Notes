import numpy as np

class KNN:
    def __init__(self):
        pass
    
    def fit(self,
            X_train : np.array,
            y_train : np.array,
            k : int) -> None:
        
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, 
                X_test : np.array) -> np.array:
        
        y_pred = [self._predict(x) for x in X_test]
        return np.array(y_pred)
    
    def _predict(self,
                 x : np.array) -> int:
        distance = [self._distance(x, x_train) for x_train in self.X_train]
        k_nearest = np.argsort(distance)[ : self.k]
        labels = [self.y_train[index] for index in k_nearest]
        return self._get_most_label(labels)    
    
    def _get_most_label(self,
                        labels : list) -> int:
        most_label = {}
        for label in labels:
            if label in most_label:
                most_label[label] += 1
            else:
                most_label[label] = 1
        return max(most_label.items() , key=lambda item : item[1])[0]
    
    def _distance(self,
                  point1 : np.array,
                  point2 : np.array) -> np.float:
        
        return np.sqrt(np.sum((point1 - point2) ** 2))