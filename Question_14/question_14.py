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
    col_education = "NAME_EDUCATION_TYPE"
    # for column in dataset.columns:print(column)
    dataset = dataset[[col_paycheck, col_gender, col_education]]
    dataset_gender_vals = list(dataset[col_gender].unique())
    dataset_education_vals = list(dataset[col_education].unique())
    
    # print(dataset_gender_vals)
    # print(dataset_education_vals)
    
    final_df = dict()
    df_sliced_by_gender = {gender : dataset[dataset[col_gender].isin([gender])] for gender in dataset_gender_vals}
    for gender, df in df_sliced_by_gender.items():
        for education in dataset_education_vals:
            final_df[(f'{gender},{education}')] = df[df[col_education].isin([education])]
    
    final_df_in_np = {k:v[col_paycheck].to_numpy() for k,v in final_df.items()}
    
    mapping_of_keys = {list(final_df_in_np.keys())[idx] : idx  for idx in range(len(final_df_in_np.keys()))}
    
    # for key in final_df.keys():print(key)
    # TODO : Fix the size of the legend and create a random exadecimal color for the graphics
    ax = plt.figure().gca()
    plt.title("Bar Plot Of Paycheck Wrt Sex and Education")
    for key,df in final_df_in_np.items():
        key_map = mapping_of_keys[key]
        # # color = random_esadecimale
        plt.bar(key_map,np.mean(df), label = key)
    plt.xlim(right = max(list(mapping_of_keys.values())))
    plt.xlabel('Gender/Education code')
    plt.ylabel('Mean Paycheck')
    plt.legend()
    plt.show()

    

    