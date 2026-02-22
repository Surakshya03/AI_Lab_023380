# Support Vector Machine (SVM) implementation using scikit-learn

import numpy as np
from sklearn import svm

# Sample training data
X = np.array([
    [2, 2],
    [4, 4],
    [4, 0],
    [0, 0]
])

# Class labels
y = np.array([1, 1, -1, -1])

# Create SVM classifier (linear kernel)
model = svm.SVC(kernel='linear')

# Train the model
model.fit(X, y)

# Test data
test = np.array([[3, 3]])

# Predict
prediction = model.predict(test)

print("Predicted class:", prediction[0])
