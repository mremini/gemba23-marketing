cookies_models = [
    'Prince',
    'Oreo',
    'Choco Bueno',
    'Petit Ecolier',
    'Mikado',
    'Granola',
    'Kinder',
    'Sables'
]
my_dissimilarity_matrix = np.array([
    [0, 5, 8, 4, 5, 3, 8, 5],
    [5, 0, 1, 5, 4, 7, 8, 3],
    [8, 1, 0, 4, 4, 3, 3, 4],
    [4, 5, 4, 0, 2, 5, 9, 8],
    [5, 4, 4, 2, 0, 5, 3, 7],
    [3, 7, 3, 5, 5, 0, 1, 9],
    [8, 8, 3, 9, 3, 1, 0, 8],
    [5, 3, 4, 8, 7, 9, 8, 0]
])
mds = MDS(dissimilarity="precomputed",random_state=63)
my_perceptual_map = mds.fit_transform(my_dissimilarity_matrix)
x = my_perceptual_map[:,0]
y = my_perceptual_map[:,1]
plt.scatter(x, y)
for i in range(0, len(cookies_models)):
    txt = cookies_models[i]
    plt.annotate(txt, [x[i], y[i]])
plt.show()