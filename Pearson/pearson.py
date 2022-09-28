import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH, PEARSON_COLUMNS
# @@

def evaluate():
    df = pd.read_csv(DATASET_PATH)

    pearson_corr = {}
    for column in PEARSON_COLUMNS:
        temp = df[["TARGET", column]].corr(method="pearson").iloc[0][1]
        pearson_corr[column] = temp

    # print(pearson_corr)
    
    




