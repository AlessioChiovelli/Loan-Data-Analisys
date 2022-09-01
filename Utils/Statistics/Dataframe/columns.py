import logging
import tqdm 
import numpy as np

# def get_stats_of_each_column(dataset):
#     columns = dataset.columns.to_list()
#     arrays = []
#     mean_values = []
#     variance_values = []
#     for column in tqdm(columns, desc = 'Converting To Array'):arrays.append(dataset[column].to_numpy())
#     for array in tqdm(arrays, desc = 'Calculating Stats'):
#         try:
#             mean_values.append(np.mean(array))
#             variance_values.append(np.var(array))
#         except:
#             mean_values.append('Stangeness! Check the data')
#             variance_values.append('Stangeness! Check the data')
#     results = {columns[idx] : {'mean': mean_values[idx] ,'variance':variance_values[idx] }for idx in range(len(columns))}
#     return results

def get_stats_of_each_column(dataset):
    description = dataset.describe(include='all').to_dict('series')
    _dict = {}
    for key,value in description.items():
        _dict[key]=value.to_dict()
    return _dict