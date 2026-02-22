# Training data for AND gate
inputs = [(0,0), (0,1), (1,0), (1,1)]
targets = [0, 0, 0, 1]

# Initial weights and bias
w1 = 0.0
w2 = 0.0
b = 0.0
learning_rate = 0.1

# Activation function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Training
for epoch in range(10):  # repeat multiple times
    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        target = targets[i]

        # Calculate output
        net_input = w1*x1 + w2*x2 + b
        output = step_function(net_input)

        # Error
        error = target - output

        # Update weights and bias
        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        b = b + learning_rate * error

print("Trained Weights:")
print("w1 =", w1)
print("w2 =", w2)
print("bias =", b)

# Testing
print("\nTesting AND Gate:")
for x1, x2 in inputs:
    net_input = w1*x1 + w2*x2 + b
    output = step_function(net_input)
    print(x1, "AND", x2, "=", output)
