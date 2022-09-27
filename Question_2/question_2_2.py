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
    
    _dict_Y = _dict.copy()
    _dict_N = _dict.copy()
    
    _dict_Y["FLAG_OWN_CAR"] = list(_dict_Y["FLAG_OWN_CAR"][1])
    _dict_N["FLAG_OWN_CAR"] = list(_dict_N["FLAG_OWN_CAR"][0])
    
    # print(_dict)
    # print(_dict_Y)
    # print(_dict_N)
    
    dataset_Y = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_Y, target_columns = target)
    dataset_N = slicing_DF_target_based_on_columns_value(dataset = dataset,columns = columns, values_of_columns = _dict_N, target_columns = target)
    print(dataset_Y)
    print(dataset_N)
    print(type(dataset_Y))
    print(type(dataset_N))
    plt.title("Histogram of people HAVING cars")
    sns.histplot(data = dataset_Y, stat = "probability", color = "green")
    plt.show()
    plt.title("Histogram of people NOT HAVING cars")
    sns.histplot(data = dataset_N, stat = "probability", color = "red")
    plt.show()
    
    num_Y = dataset_Y["TARGET"].value_counts().to_dict()
    num_N = dataset_N["TARGET"].value_counts().to_dict()
    labels = []
    values = []
    
    if len(list(num_Y.values())) != 0:
        num_Y = {k : v/len_df for k,v in num_Y.items()} 
        labels.extend(["Y_0","Y_1"])
        values.extend(list(num_Y.values()))
        
    if len(list(num_N.values())) != 0:
        num_N = {k : v/len_df for k,v in num_N.items()} 
        labels.extend(["N_0","N_1"])
        values.extend(list(num_N.values()))
        
    plt.title("Histogram of (un)Solvent clients With/Without Car(s)")
    plt.pie(values, labels = labels, shadow = True, autopct='%1.1f%%')
    plt.show()
    
if __name__ == '__main__':
    evaluate()


