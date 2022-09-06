import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.Statistics.Dataframe.slicing import *
# @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    """Evaluate the question, and try to give an answer.
    """
    columns = ['CODE_GENDER','FLAG_OWN_CAR','CNT_CHILDREN','NAME_EDUCATION_TYPE']
    target = ['TARGET']
    dataset = pd.read_csv(DATASET_PATH)
    _dict = unique_values_of_cols(dataset,columns)
    df_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset, columns = columns, values_of_columns = _dict, target_columns = target)
    print(df_sliced)
    
    
    # print(dataset)
    # for k,v in unique_values_of_cols(dataset, columns).items:
    #     print(f'key:{k} value:{v}')
    # df_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = {}, target_column : str)
    
if __name__ == '__main__':
    evaluate()


