import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from tqdm import tqdm,trange
from random import uniform
import logging




# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.IO.file import pretty_print_of_dict 
from Utils.Statistics.Dataframe.columns import get_stats_of_each_column,get_percentage_of_NaN_in_columns,filter_NaN_values_by_threshold, distribution_of_values_in_column
# @@

logging.basicConfig(filename="bigdara.log",level=logging.DEBUG)

def apply_PCA(dataset, columns_to_include, n_components = 2):
    X = dataset[columns_to_include]
    pca = PCA(n_components=3, copy = True)
    pca.fit(X)
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)


def replace_by_interpolation(dataset, columns_to_replace, **dict_of_val_range_cols):
    '''
    dict_of_val_range_cols needs to be something like:
    {
        column:
            {
                - value: ...
                - range: ...
            }
    }
    '''
    for column in columns_to_replace:
        dataset[column].replace(np.nan, dict_of_val_range_cols[column]['value'] + uniform(-1,1) * dict_of_val_range_cols[column]['range'])
    return dataset

if __name__ == '__main__':
    dataset = pd.read_csv(DATASET_PATH)
    
    columns_filtered = filter_NaN_values_by_threshold(dataset = dataset, threshold = 10)
    stats = get_stats_of_each_column(dataset)
    distribution_of_values_in_column(dataset,"TARGET")
    pretty_print_of_dict(stats, file_name="initial_stats")
    
    cols_desired = [
        'CNT_CHILDREN',
        'AMT_INCOME_TOTAL',
        'AMT_CREDIT'
    ]
    apply_PCA(dataset, cols_desired)
    
    
    
    
    
    
    # print(columns_filtered)
    

