import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
from tqdm import tqdm,trange
from random import uniform
import logging

# @@ Personal Libraries
from Utils.IO.file import pretty_print_of_dict 
from Utils.Statistics.Dataframe.columns import get_stats_of_each_column
# @@

logging.basicConfig(filename="bigdara.log",level=logging.DEBUG)
 
def apply_PCA(dataset, columns_to_include, n_components = 2):
    X = dataset[columns_to_include]
    pca = PCA(n_components=3, copy = True)
    pca.fit(X)
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)

def nulls(dataset):
    return {col: dataset[col].isnull().sum() * 100 / dataset.shape[0] for col in dataset.columns.to_list()}

def filter_NaN_values_by_threshold(dataset, threshold = 20):
    null_columns = nulls(dataset)
    filtered_cols = {k: v for k, v in null_columns.items() if v < threshold}
    # for k,v in null_columns.items():print(f'column: {k} percentage of none values: {v}')
    # for k,v in filtered_cols.items():print(f'column: {k} percentage of none values: {v}')
    print(len(null_columns))
    print(len(filtered_cols))
    return null_columns

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
    path = "data/loan_data.csv"

    dataset = pd.read_csv(path)

    # n_rows,n_columns = dataset.shape
    # columns = dataset.columns.to_list()
    # columns_filtered = filter_NaN_values_by_threshold(dataset = dataset, threshold = 10)
    stats = get_stats_of_each_column(dataset)
    pretty_print_of_dict(stats, file_name="initial_stats")
    
    cols_desired = [
        'CNT_CHILDREN',
        'AMT_INCOME_TOTAL',
        'AMT_CREDIT'
    ]
    apply_PCA(dataset, cols_desired)
    
    
    
    
    
    
    # print(columns_filtered)
    

