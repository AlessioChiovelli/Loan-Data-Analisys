import logging
import numpy as np
import pandas as pd
from typing import Dict, List

def get_stats_of_each_column(dataset: pd.DataFrame) -> Dict:
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


def get_percentage_of_NaN_in_columns(dataset: pd.DataFrame) -> pd.Series:
    """Evaluate the percentage of NaN elements in each column of the dataset

    Args:
        dataset (pd.Dataframe): The source dataset

    Returns:
        pd.Series: A series containing the percentage of each column of the dataset
    """    
    percentage_of_NaN_for_column = dataset.isnull().sum() *100/dataset.shape[0]
    return percentage_of_NaN_for_column

def filter_NaN_values_by_threshold(dataset: pd.DataFrame, percentage_threshold: float = 20.0) -> pd.Series:
    """Retrieve only the columns of the dataset that have less than the given threshold of NaN elements

    Args:
        dataset (pd.Dataframe): The source dataset
        threshold (int, optional): The threshold. Defaults to 20.

    Returns:
        pd.Series: The columns that match the condition
    """    
    null_columns = get_percentage_of_NaN_in_columns(dataset)
    filtered_cols = null_columns[null_columns < percentage_threshold]
    return filtered_cols

def distribution_of_values_in_column(dataset: pd.DataFrame, target_column: str, percentage: bool = True) -> pd.Series:
    """Evaluate the distribution of each different value for a given column

    Args:
        dataset (pd.DataFrame): Source dataset
        target_column (str): Column for which the distribution is evaluated
        percentage (bool, optional): Whether the distribution is a percentage or absolute value
        
    Returns:
        pd.Series: The distribution in percentage of each different value 
    """    
    counter = dataset.groupby(target_column, as_index=False)[target_column].count()
    return (counter / dataset.shape[0])*100 if percentage else counter

def balance_dataset_wrt_column_values(dataset: pd.DataFrame, target_column: str, bf_cutting: str = True) -> pd.DataFrame:
    """Balance a given dataframe wrt different values of a column

    Args:
        dataset (pd.DataFrame): Source dataframe
        target_column (str): The column for which the balance is evaluated
        bf_cutting (str, optional): Try to balance with a percentage or absolute value. Defaults to True.

    Returns:
        pd.DataFrame: _description_
    """    
    value_distribution = distribution_of_values_in_column(dataset, target_column, percentage=False)
    threshold = 1000 # TODO: shold be absolute or a percentage???
    if bf_cutting: threshold = min(value_distribution[target_column])
    balanced_dataset = dataset.groupby(target_column, as_index=False).apply(lambda group: group.sample(frac=1)[:threshold])
    return balanced_dataset
    

################################################################
# EXAMPLE #################################
# NOT INTENDED FOR PRODUCTION CODE #
if __name__ == '__main__':
    import os
    import matplotlib.pyplot as plt
    import seaborn as sns 
    
    dataset = pd.read_csv("data/loan_data.csv")
    print(os.getcwd())


    def bar_plot(x, y):
        g = sns.barplot(x=x, y=y)
        plt.show()

    # useful for graphically showing a correlation between two columns
    def scatter_plot(dataset: pd.DataFrame, x: str, y: str) -> None:
        diagram = dataset.plot.scatter(x = x, y = y)
        plt.show()

    # TODO sarebbe meglio passargli in input invece che tutto il dataset un dataset ripulito da outliers 
    # oppure limitare la visualizzazione a un certo range stabilito a posteriori
    scatter_plot(dataset, "CNT_CHILDREN", "AMT_INCOME_TOTAL")

    # UNBALANCED DATA wrt TARGET
    value_distribution = distribution_of_values_in_column(dataset, 'TARGET', percentage=False)
    bar_plot(value_distribution.index,value_distribution["TARGET"].tolist())
    
    # BALANCE DATA wrt TARGET
    dataset = balance_dataset_wrt_column_values(dataset, 'TARGET')
    value_distribution = distribution_of_values_in_column(dataset, "TARGET", percentage=False)
    bar_plot(value_distribution.index,value_distribution["TARGET"].tolist())