# Perceptron training for NOT gate

# Training data
inputs = [0, 1]
targets = [1, 0]

# Initialize weight and bias
w = 0.0
b = 0.0
learning_rate = 0.1

# Step activation function
def step(x):
    return 1 if x >= 0 else 0

# Training
for epoch in range(10):
    for i in range(len(inputs)):
        x = inputs[i]
        target = targets[i]

        net = w * x + b
        output = step(net)

        error = target - output

        w = w + learning_rate * error * x
        b = b + learning_rate * error

# Testing
for x in inputs:
    net = w * x + b
    print("NOT", x, "=", step(net))
