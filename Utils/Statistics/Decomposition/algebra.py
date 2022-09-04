from sklearn.decomposition import PCA

def apply_PCA(dataset, columns_to_include, n_components=2):
    X = dataset[columns_to_include]
    pca = PCA(n_components=3, copy=True)
    pca.fit(X)
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)