import numpy as np

# Input
X = np.array([[0,0],[0,1],[1,0],[1,1]])

# Target
Y = np.array([[0],[1],[1],[0]])

# Random weights
np.random.seed(1)
W1 = np.random.rand(2,2)
W2 = np.random.rand(2,1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

# Training
for epoch in range(10000):

    # Forward pass
    hidden = sigmoid(np.dot(X, W1))
    output = sigmoid(np.dot(hidden, W2))

    # Error
    error = Y - output

    # Backpropagation
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden)

    # Update weights
    W2 += hidden.T.dot(d_output)
    W1 += X.T.dot(d_hidden)

print("Final Output:")
print(np.round(output))
