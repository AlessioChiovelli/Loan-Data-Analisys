import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH


def evaluate():
    df = pd.read_csv(DATASET_PATH)
    #           education,      number of children, status (e.g. married), insolvency
    df = df[["NAME_EDUCATION_TYPE", "CNT_CHILDREN", "NAME_FAMILY_STATUS", "TARGET"]]

    # Cleaning some data, manually and arbitrarily excluding outliers (families with more than 5 children are a small population, 
    # idem for academics and Unknown family status are just 2 people)
    df2 = df.loc[(df["CNT_CHILDREN"] <= 4) & (df["NAME_EDUCATION_TYPE"] != 'Academic degree') & (df["NAME_FAMILY_STATUS"] != "Unknown")]
    #df2["NAME_FAMILY_STATUS"].value_counts().plot(kind="pie")
    #plt.show()

    # df2 = df2.groupby(["CNT_CHILDREN", "NAME_FAMILY_STATUS", "NAME_EDUCATION_TYPE"]).filter(lambda df: df[["CNT_CHILDREN", "NAME_FAMILY_STATUS", "NAME_EDUCATION_TYPE"]].count()>30) # da rimuovere
    df3 = df2.groupby(["CNT_CHILDREN", "NAME_FAMILY_STATUS", "NAME_EDUCATION_TYPE"]).mean()*100
    df4 = df3.unstack(level=-1).plot.bar()
    print(df4)
    #df3["NAME_EDUCATION_TYPE"].plot(figsize = (8,8), title="Insolvency rate wrt Education Level grouped by Family Status and number of children")
    plt.tight_layout()
    plt.show()
        

