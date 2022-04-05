import numpy as np
inertia_values = []
all_k = np.arange(1,7)
for k in all_k:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(points_scaled)
    inertia_values.append(kmeans.inertia_)
plt.plot(all_k, inertia_values)
plt.show()
optimal_k = 4