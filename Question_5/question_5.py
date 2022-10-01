import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.Statistics.Dataframe.slicing import *
# @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    
    dataset = pd.read_csv("data/loan_data.csv")
    # len_df = dataset.shape[0]
    dataset["APPROX_AGE"] = (dataset["DAYS_BIRTH"] /
                                365).apply(lambda element: abs(int(element)))
    
    df = dataset[["TARGET","APPROX_AGE"]]
    
    df_solvent = df.loc[df["TARGET"] == 0]["APPROX_AGE"]
    df_unsolvent = df.loc[df["TARGET"] == 1]["APPROX_AGE"]
    
    # print(df_solvent)
    # print(df_unsolvent)
    
    
    
    # dict_of_info = df.value_counts().to_dict()
    
    # dict_of_solving_clients = dict()
    # dict_of_unsolving_clients = dict()
    
    # for k,v in dict_of_info.items():
    #     if k[0] == 0:
    #         if k[0] in list(dict_of_solving_clients.keys()):
    #             dict_of_solving_clients[k[-1]] += v
    #         else:
    #             dict_of_solving_clients[k[-1]] = v
    #     else:
    #         if k[0] in list(dict_of_unsolving_clients.keys()):
    #             dict_of_unsolving_clients[k[-1]] += v
    #         else:
    #             dict_of_unsolving_clients[k[-1]] = v
    
    # print(dataset.columns)
    # print(df)
    # for k,v in dict_of_solving_clients.items():print(f'key: {k}\t\tvalue: {v}')
    # print(3 * '\n', 100 * '*', 3 * '\n')
    # for k,v in dict_of_unsolving_clients.items():print(f'key: {k}\t\tvalue: {v}')
    
    
    plt.title('Clients wrt Age')
    sns.histplot(df_solvent, bins = np.arange(18,70), color = "Green", label = "Solvent")
    sns.histplot(df_unsolvent, bins = np.arange(18,70), color = "Red", label = "Unsolvent")
    plt.legend()
    plt.show()
    
    
if __name__ == '__main__':
    evaluate()


