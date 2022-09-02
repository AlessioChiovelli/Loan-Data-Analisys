import logging
import numpy as np

def get_stats_of_each_column(dataset):
    """Retrieve statistics of each column of the dataset

    Args:
        dataset (pd.Dataframe): The source dataset

    Returns:
        dict: Dictionary of column statistics, in this format:
                {
                    "column":
                        {
                            "stats_1":value,...
                        },...
                }
    """    
    description = dataset.describe(include='all').to_dict('series')
    _dict = {}
    for key,value in description.items():
        _dict[key]=value.to_dict()
    return _dict


def get_percentage_of_NaN_in_columns(dataset):
    """Evaluate the percentage of NaN elements in each column of the dataset

    Args:
        dataset (pd.Dataframe): The source dataset

    Returns:
        pd.Series: A series containing the percentage of each column of the dataset
    """    
    percentage_of_NaN_for_column = dataset.isnull().sum() *100/dataset.shape[0]
    return percentage_of_NaN_for_column

def filter_NaN_values_by_threshold(dataset, threshold = 20):
    """Retrieve only the columns of the dataset that have less than the given threshold of NaN elements

    Args:
        dataset (pd.Dataframe): The source dataset
        threshold (int, optional): The threshold. Defaults to 20.

    Returns:
        pd.Series: The columns that match the condition
    """    
    null_columns = get_percentage_of_NaN_in_columns(dataset)
    filtered_cols = null_columns[null_columns < 20]
    return filtered_cols

def distribution_of_values_in_column(dataset, target_column):
    """_summary_

    Args:
        dataset (_type_): _description_
        target_column (_type_): _description_
    """    
    return (dataset.groupby(target_column)[target_column].count() / dataset.shape[0])*100 

