# Simple Perceptron Demo

import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_pred = 1 if linear_output >= 0 else -1
                update = self.lr * (y[idx] - y_pred)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.where(linear_output >= 0, 1, -1)


def main():
    # Example dataset: OR logic gate
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([-1, 1, 1, 1])

    percep = Perceptron(learning_rate=0.1, n_iters=10)
    percep.fit(X, y)
    predictions = percep.predict(X)

    print("Predictions:", predictions)
    print("True labels:", y)
    accuracy = np.mean(predictions == y)
    print(f"Accuracy: {accuracy*100:.2f}%")


if __name__ == "__main__":
    main()
