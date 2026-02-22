# k-Nearest Neighbors (kNN) implementation from scratch

import math
from collections import Counter

# Sample dataset (features + label)
dataset = [
    ([2, 4], 'A'),
    ([4, 6], 'A'),
    ([4, 4], 'B'),
    ([6, 2], 'B'),
    ([6, 4], 'B')
]

# Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# kNN algorithm
def knn(data, test_point, k):
    distances = []
    
    for features, label in data:
        dist = euclidean_distance(features, test_point)
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])
    
    k_nearest_labels = [label for (_, label) in distances[:k]]
    
    return Counter(k_nearest_labels).most_common(1)[0][0]

# Test point
test_point = [5, 5]
k = 3

prediction = knn(dataset, test_point, k)
print("Predicted Class:", prediction)
