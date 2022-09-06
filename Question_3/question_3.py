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
    columns = ['FLAG_OWN_CAR']
    target = ['TARGET']
    dataset = pd.read_csv(DATASET_PATH)
    len_df = dataset.shape[0]
    _dict = unique_values_of_cols(dataset,columns)
    print(_dict)
    
    
    _dict_Y = _dict.copy()
    _dict_N = _dict.copy()
    
    _dict_Y["FLAG_OWN_CAR"] = list(_dict_Y["FLAG_OWN_CAR"][1])
    _dict_N["FLAG_OWN_CAR"] = list(_dict_N["FLAG_OWN_CAR"][0])
    
    # print(_dict_M)
    # print(_dict_F)
    
    dataset_Y = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_Y, target_columns = ['TARGET'])
    dataset_N = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_N, target_columns = ['TARGET'])
    
    # print(dataset_M)
    # print(dataset_F)
    # print(dataset_XNA)
    
    plt.title("Histogram of people HAVING cars")
    sns.histplot(data = dataset_Y, stat = "probability")
    plt.show()
    plt.title("Histogram of people NOT HAVING cars")
    sns.histplot(data = dataset_N, stat = "probability")
    plt.show()
    # print(dataset)
    # for k,v in unique_values_of_cols(dataset, columns).items:
    #     print(f'key:{k} value:{v}')
    # df_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = {}, target_column : str)
    
if __name__ == '__main__':
    evaluate()


