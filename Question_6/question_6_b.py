from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH
from Utils.Plot.make_plot import pie_chart as pie
# @@



def evaluate():
    dataset = pd.read_csv(DATASET_PATH)
    df = dataset[["NAME_EDUCATION_TYPE", "TARGET"]]
    
    '''
    0: Secondary / secondary special
    1: Higher education
    2: Incomplete higher
    3: Lower secondary
    4: Academic degree
    '''
    
    df_S = df.loc[df["TARGET"] == 0]
    df_U = df.loc[df["TARGET"] == 1]
    
    
    df_S_0 = df_S.loc[df_S["NAME_EDUCATION_TYPE"] == "Secondary / secondary special"]["NAME_EDUCATION_TYPE"]
    df_S_1 = df_S.loc[df_S["NAME_EDUCATION_TYPE"] == "Higher education"]["NAME_EDUCATION_TYPE"]
    df_S_2 = df_S.loc[df_S["NAME_EDUCATION_TYPE"] == "Incomplete higher"]["NAME_EDUCATION_TYPE"]
    df_S_3 = df_S.loc[df_S["NAME_EDUCATION_TYPE"] == "Lower secondary"]["NAME_EDUCATION_TYPE"]
    df_S_4 = df_S.loc[df_S["NAME_EDUCATION_TYPE"] == "Academic degree"]["NAME_EDUCATION_TYPE"]
    
    df_U_0 = df_U.loc[df_U["NAME_EDUCATION_TYPE"] == "Secondary / secondary special"]["NAME_EDUCATION_TYPE"]
    df_U_1 = df_U.loc[df_U["NAME_EDUCATION_TYPE"] == "Higher education"]["NAME_EDUCATION_TYPE"]
    df_U_2 = df_U.loc[df_U["NAME_EDUCATION_TYPE"] == "Incomplete higher"]["NAME_EDUCATION_TYPE"]
    df_U_3 = df_U.loc[df_U["NAME_EDUCATION_TYPE"] == "Lower secondary"]["NAME_EDUCATION_TYPE"]
    df_U_4 = df_U.loc[df_U["NAME_EDUCATION_TYPE"] == "Academic degree"]["NAME_EDUCATION_TYPE"]
    
    plt.title('Clients wrt education')
    
    sns.histplot(df_S_0, label = "Solvent Secondary / secondary special", color = "#00ff00")
    sns.histplot(df_S_1, label = "Solvent Higher education", color = "#00e500")
    sns.histplot(df_S_2, label = "Solvent Incomplete higher", color = "#00cc00")
    sns.histplot(df_S_3, label = "Solvent Lower secondary", color = "#00b200")
    sns.histplot(df_S_4, label = "Solvent Academic degree", color = "#009900")
    
    sns.histplot(df_U_0, label = "Unsolvent Secondary / secondary special", color = "#f44336")
    sns.histplot(df_U_1, label = "Unsolvent Higher education", color = "#db3c30")
    sns.histplot(df_U_2, label = "Unsolvent Incomplete higher", color = "#c3352b")
    sns.histplot(df_U_3, label = "Unsolvent Lower secondary", color = "#aa2e25")
    sns.histplot(df_U_4, label = "Unsolvent Academic degree", color = "#922820")
    plt.legend()
    plt.show()
    
    