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

    plt.figure()
    heatmap = sns.heatmap(df[["TARGET"]+PEARSON_COLUMNS].corr(method="pearson"), vmin=-1, vmax=1, cmap='BrBG')
    # save heatmap as .png file
    # dpi - sets the resolution of the saved image in dots/inches
    # bbox_inches - when set to 'tight' - does not allow the labels to be cropped
    plt.savefig('heatmap.png', dpi=400, bbox_inches='tight')
    
    




