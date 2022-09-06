<<<<<<< HEAD
from turtle import color
=======
>>>>>>> a2ed8d43a297f01dab418594c2e49beb62ca0755
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH
# @@


def evaluate():
    """Evaluate the question, and try to give an answer.
    """    
    dataset = pd.read_csv(DATASET_PATH)

    # Prepare plot
    figure, axes = plt.subplots(1, 2,  figsize=(15, 15))
    figure.suptitle('Famility status and Insolvency')
    axes[0].set_title('Family status distribution')
    axes[1].set_title('Ratio of Insolvency for each Family Status')
    
    # Distribution of famility status
    family_status_count = dataset["NAME_FAMILY_STATUS"].value_counts()
    axes[0].pie(family_status_count.values.tolist(), labels= family_status_count.index.tolist(),autopct='%1.1f%%')
    
    # Evaluate ratio between the positive TARGET and the total number of TARGET for each family status
    ratio =  dataset.groupby("NAME_FAMILY_STATUS").apply(lambda family_group: (100*family_group[family_group.TARGET == 1].count()/family_group["TARGET"].count())["TARGET"])
    axes[1].set_ylabel("Percentage of Insolvency Ratio")
    sns.barplot(x=ratio.index.tolist(), y=ratio.values.tolist(),ax=axes[1])
    plt.show()
    

