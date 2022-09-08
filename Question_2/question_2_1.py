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
    _dict = unique_values_of_cols(dataset,columns)
    len_df = dataset.shape[0]

    
    # dataset_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict, target_columns = ['TARGET'])
    
    # plt.title("Histogram Divided By Sex")
    # sns.histplot(data = dataset_sliced, stat = "probability", hue = "sex")
    # plt.show()
    
    _dict_M = _dict.copy()
    _dict_F = _dict.copy()
    _dict_XNA = _dict.copy()
    
    _dict_M["CODE_GENDER"] = list(_dict_M["CODE_GENDER"][0])
    _dict_F["CODE_GENDER"] = list(_dict_F["CODE_GENDER"][1])
    _dict_XNA["CODE_GENDER"] = list(_dict_XNA["CODE_GENDER"][2])
    
    dataset_M = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_M, target_columns = target)
    dataset_F = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_F, target_columns = target)
    dataset_XNA = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_XNA, target_columns = target)
    
    plt.title("Histogram of M")
    sns.histplot(data = dataset_M, stat = "probability")
    plt.show()
    plt.title("Histogram of F")
    sns.histplot(data = dataset_F, stat = "probability")
    plt.show()
    plt.title("Histogram of XNA")
    sns.histplot(data = dataset_XNA, stat = "probability")
    plt.show()
    
    num_M = dataset_M["TARGET"].value_counts().to_dict()
    num_F = dataset_F["TARGET"].value_counts().to_dict()
    num_XNA = dataset_XNA["TARGET"].value_counts().to_dict()
    labels = []
    values = []
    
    if len(list(num_M.values())) != 0:
        num_M = {k : v/len_df for k,v in num_M.items()} 
        labels.extend(["M_0","M_1"])
        values.extend(list(num_M.values()))
        
    if len(list(num_F.values())) != 0:
        num_F = {k : v/len_df for k,v in num_F.items()} 
        labels.extend(["F_0","F_1"])
        values.extend(list(num_F.values()))

    if len(list(num_XNA.values())) != 0:
        num_XNA = {k : v/len_df for k,v in num_XNA.items()} 
        labels.extend(["XNA_0","XNA_1"])
        values.extend(list(num_XNA.values()))
    
    plt.pie(values, labels = labels, shadow = True, autopct='%1.1f%%')
    plt.show()
    
if __name__ == '__main__':
    evaluate()


