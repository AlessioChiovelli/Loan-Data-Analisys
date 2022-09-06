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
    columns = ['CODE_GENDER']
    target = ['TARGET']
    dataset = pd.read_csv(DATASET_PATH)
    len_df = dataset.shape[0]
    _dict = unique_values_of_cols(dataset,columns)
    
    dataset_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict, target_columns = ['TARGET'])
    
    plt.title("Histogram Divided By Sex")
    sns.histplot(data = dataset_sliced, stat = "probability", hue = "sex")
    plt.show()
    
    # _dict_M = _dict.copy()
    # _dict_F = _dict.copy()
    # _dict_XNA = _dict.copy()
    
    # # print(_dict_M)
    # # print(_dict_F)
    # # print(_dict_XNA)
    
    # _dict_M["CODE_GENDER"] = list(_dict_M["CODE_GENDER"][0])
    # _dict_F["CODE_GENDER"] = list(_dict_F["CODE_GENDER"][1])
    # _dict_XNA["CODE_GENDER"] = list(_dict_XNA["CODE_GENDER"][2])
    
    # dataset_M = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_M, target_columns = ['TARGET'])
    # dataset_F = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_F, target_columns = ['TARGET'])
    # dataset_XNA = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_XNA, target_columns = ['TARGET'])
    
    # print(dataset_M)
    # print(dataset_F)
    # print(dataset_XNA)
    
    # plt.title("Histogram of M")
    # sns.histplot(data = dataset_M, stat = "probability", hue = "sex")
    # plt.show()
    # plt.title("Histogram of F")
    # sns.histplot(data = dataset_F, stat = "probability", hue = "sex")
    # plt.show()
    # plt.title("Histogram of XNA")
    # sns.histplot(data = dataset_XNA, stat = "probability", hue = "sex")
    # plt.show()
    
    
    # print(dataset)
    # for k,v in unique_values_of_cols(dataset, columns).items():
    #     print(f'key:{k} value:{v}')
    
    
    # df_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset, columns = columns, values_of_columns = _dict, target_columns = target)
    # print(df_sliced)
    
if __name__ == '__main__':
    evaluate()


