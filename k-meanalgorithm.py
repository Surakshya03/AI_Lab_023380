# K-Means Clustering from scratch (without sklearn)

import random
import math

# Sample dataset
data = [
    [2, 4],
    [4, 6],
    [4, 4],
    [6, 2],
    [6, 4],
    [8, 6]
]

k = 2  # number of clusters

# Euclidean distance
def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# Initialize centroids randomly
centroids = random.sample(data, k)

for iteration in range(10):
    clusters = [[] for _ in range(k)]
    
    # Assign points to nearest centroid
    for point in data:
        distances = [distance(point, centroid) for centroid in centroids]
        min_index = distances.index(min(distances))
        clusters[min_index].append(point)
    
    # Update centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            mean_x = sum(point[0] for point in cluster) / len(cluster)
            mean_y = sum(point[1] for point in cluster) / len(cluster)
            new_centroids.append([mean_x, mean_y])
        else:
            new_centroids.append(random.choice(data))
    
    centroids = new_centroids

print("Final Centroids:")
for centroid in centroids:
    print(centroid)

print("\nClusters:")
for i, cluster in enumerate(clusters):
    print("Cluster", i + 1, ":", cluster)
