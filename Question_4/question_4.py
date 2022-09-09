import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.Statistics.Dataframe.slicing import *
# @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    """Evaluate the question, and try to give an answer.
    """
    # columns = ['CODE_GENDER']
    # target = ['TARGET']
    dataset = pd.read_csv(DATASET_PATH)
    col_paycheck = "AMT_INCOME_TOTAL"
    col_gender = "CODE_GENDER"
    dataset = dataset[[col_paycheck, col_gender]]
    dataset_gender_vals = list(dataset[col_gender].unique())
    gender_income_dict = {gender : dataset[dataset[col_gender].isin([gender])][col_paycheck] for gender in dataset_gender_vals}
    # for k,v in gender_income_dict.items():
    #     print(f'KEY {k}')
    #     print(3*'\n',3*'\n')
    #     print(f'DATASET')
    #     print(type(v))
    #     print(3*'\n',100 * '=',3*'\n')
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax = plt.figure().gca()
    plt.title("Bar Plot Of Paycheck Wrt Sex")
    for idx in range(len(dataset_gender_vals)):
        gender = dataset_gender_vals[idx]
        # color = random_esadecimale
        plt.bar(idx,np.mean(gender_income_dict[gender].to_numpy()), label = gender)
    plt.xlabel('Gender code')
    plt.ylabel('Mean Paycheck')
    plt.legend()
    plt.show()
    
    # TODO : Fix the size of the legend and create a random exadecimal color for the graphics
    ax = plt.figure().gca()
    plt.title("ErrorBar Plot Of Paycheck Wrt Sex")
    for idx in range(len(dataset_gender_vals)):
        gender = dataset_gender_vals[idx]
        # color = random_esadecimale
        plt.errorbar(idx,np.mean(gender_income_dict[gender].to_numpy()), np.std(gender_income_dict[gender].to_numpy()),fmt='o', linewidth=2, capsize=6, label = gender)
    plt.xlabel('Gender code')
    plt.ylabel('Mean Paycheck')
    plt.legend()
    plt.show()
    
    # gender_income_stats_dict = {gender: df.value_counts().to_dict() for gender,df in gender_income_dict.items()}
    # for k,v in gender_income_stats_dict.items():print(100 * '=',f'GENDER CODE\t\t{k}', 3*'\n', f'{v}','\n', 100 * '=','\n')
    
    # plt.title("Histogram Of Paycheck Wrt Sex")
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # for gender_df in gender_income_dict.values():
    #     sns.histplot(data = gender_df)
    # for gender in dataset_gender_vals:
        # sns.histplot(data = gender_income_dict[gender], label = gender, bins = "auto")
    # plt.xlabel('Gender code')
    # plt.ylabel('Mean Paycheck')
    # plt.legend()
    # plt.show()
    # sns.histplot(data = dataset)
    # plt.show()
    # print(dataset)
    # for col in dataset.columns:print(col)
    