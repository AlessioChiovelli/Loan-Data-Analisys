import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import MaxNLocator

# @@ Personal Libraries
from CONFIG import DATASET_PATH
# from Utils.Statistics.Dataframe.slicing import *
# @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    """Evaluate the question, and try to give an answer.
    """
    cols_to_slice = ["TARGET", "CNT_CHILDREN"]
    dataset = pd.read_csv(DATASET_PATH)
    list_of_values_for_children = list(dataset["CNT_CHILDREN"].value_counts().to_dict().keys())
    len_df = dataset.shape[0]
    df_sliced = dataset[cols_to_slice]
    df_0 = df_sliced[df_sliced["TARGET"].isin([0])]
    df_1 = df_sliced[df_sliced["TARGET"].isin([1])]
    df_0_results = df_0["CNT_CHILDREN"].value_counts().to_dict()
    df_1_results = df_1["CNT_CHILDREN"].value_counts().to_dict()
    df_0_results = {k : 100 * v/ len_df for k,v in df_0_results.items()}
    df_1_results = {k : 100 * v/ len_df for k,v in df_1_results.items()}
    bins = [i for i in range(0,np.max(list_of_values_for_children)+1)]
    print(df_0_results)
    print(df_1_results)
    labels_0,labels_1 = list(df_0_results.keys()),list(df_1_results.keys())
    percs_0,percs_1 = list(df_0_results.values()),list(df_1_results.values())
    ax = plt.figure().gca()
    plt.title("Bar chart of (Un)Solvent clients wrt children counts")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.bar(np.array(labels_0),np.array(percs_0), color = 'green', label = "Solving Clients")
    plt.bar(np.array(labels_1),np.array(percs_1), color = 'red', label = "Unsolving Clients")
    plt.xlabel('Children Counts')
    plt.ylabel('Perc')
    plt.legend()
    plt.show()
    
    
    
if __name__ == '__main__':
    evaluate()


