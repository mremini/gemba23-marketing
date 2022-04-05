optimal_clusters = KMeans(n_clusters=4, random_state=0)
labels = optimal_clusters.fit_predict(points_scaled)
plot_clusters(points_scaled, labels, optimal_clusters.cluster_centers_)