import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH


def evaluate():
    df = pd.read_csv(DATASET_PATH)
    #      number of children, status (e.g. married), insolvency
    df = df[["CNT_CHILDREN", "NAME_FAMILY_STATUS", "TARGET"]]
    # counting_temp = df.loc[(df.CNT_CHILDREN == 4) & (df.NAME_FAMILY_STATUS == "Civil marriage" )].count()
    # print(f"There are {counting_temp.TARGET} individual who are in a civil marriage and have 4 children")

    # # Cleaning some data, manually and arbitrarily excluding outliers (families with more than 4 children are a small population, 
    # # idem for academics and Unknown family status are just 2 people)
    # df2 = df.loc[(df["CNT_CHILDREN"] <= 4) & (df["NAME_FAMILY_STATUS"] != "Unknown")]
    # #df2["NAME_FAMILY_STATUS"].value_counts().plot(kind="pie")
    # #plt.show()

    # df3 = df2.groupby(["CNT_CHILDREN", "NAME_FAMILY_STATUS"]).mean()*100
    # df4 = df3.unstack(level=-1).plot.bar()
    
    
    minimum_group_size = 50
    grouped = df.groupby(by=["CNT_CHILDREN", "NAME_FAMILY_STATUS"]) 
    df_more100 = grouped.filter(lambda x: x.TARGET.count() > minimum_group_size)
    df_grouped = df_more100.groupby(["CNT_CHILDREN", "NAME_FAMILY_STATUS"]).mean()*100
    df_grouped.unstack(level=-1).plot.bar()
    
    plt.tight_layout()
    plt.show()
