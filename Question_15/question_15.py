import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA

# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.Statistics.Dataframe.slicing import *
# @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    """Evaluate the question, and try to give an answer.
    """
    n_components = 5
    n_bits = [8,16,32,64,128,256]
    _dtypes = ['int8','int16','int32','int64','uint8','uint16','uint32','uint64','float8','float16','float32','float64','float128','complex64','complex128','complex256']
    pca = PCA(n_components=n_components)
    # dataset = pd.read_csv(DATASET_PATH).to_numpy()
    dataset = pd.read_csv(DATASET_PATH)
    numeric_columns = []
    for column in list(dataset.columns):
        if str(dataset[column].dtype) in _dtypes:
            numeric_columns.append(column)
    dataset = dataset[numeric_columns]
    dataset = dataset.fillna(-1)
    print(dataset.shape)
    # print(dataset)
    # .to_numpy(dtype = np.float64)
    pca.fit_transform(dataset)
    # print(pca.explained_variance_ratio_)
    # print(pca.singular_values_)
    # print(pd.DataFrame(pca.components_,columns=data_scaled.columns,index = ['PC-1','PC-2']))
    print(pca.components_.shape)
    