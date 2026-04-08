import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
points = np.array([
    [1, 1], [1.2, 1.1], [0.8, 0.9],   # cluster 1
    [5, 5], [5.2, 5.1], [4.8, 4.9],   # cluster 2
    [8, 1],                            # noise
    [9, 9],                            # noise
    [0, 5],                            # noise
    [6, 2]                             # borderline
])
eps = 0.6
min_samples = 2

db = DBSCAN(eps=eps, min_samples=min_samples)
labels = db.fit_predict(points)
plt.figure(figsize=(8,6))

unique_labels = set(labels)

for label in unique_labels:
    if label == -1:
        plt.scatter(points[labels == label, 0],
                    points[labels == label, 1],
                    c='red', s=80, label='Noise')
    else:
        plt.scatter(points[labels == label, 0],
                    points[labels == label, 1],
                    s=80, label=f'Cluster {label}')
for point in points:
    circle = plt.Circle((point[0], point[1]), eps,
                        color='gray', fill=False, linestyle='dashed', alpha=0.4)
    plt.gca().add_patch(circle)

plt.title(f"DBSCAN Demo (eps={eps}, min_samples={min_samples})")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()