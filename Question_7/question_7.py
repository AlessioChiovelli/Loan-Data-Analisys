from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH



def evaluate():
    df = pd.read_csv(DATASET_PATH)
    edu, target, age = "NAME_EDUCATION_TYPE", "TARGET", "DAYS_BIRTH"  

    # data cleaning
    df = df[[target, edu, age]]
    df[age] = df[age].map(lambda days: (- days // 365))
    df.rename(columns={"DAYS_BIRTH": "AGE", 
        "NAME_EDUCATION_TYPE": "EDU"}, inplace=True)  # shortening long words...

    '''  df's head looks like this now:
    
       TARGET                            EDU  AGE
    0       1  Secondary / secondary special   25
    1       0               Higher education   45
    2       0  Secondary / secondary special   52
    3       0  Secondary / secondary special   52
    4       0  Secondary / secondary special   54
    ...

    '''

    # this dictionary's only purpose is to show the order of 
    # education level by ISCED scale if you're unfamiliar with it
    edu_levels = {
        'Secondary / secondary special': 3, 
        'Higher education': 5, 
        'Incomplete higher': 4, 
        'Lower secondary': 2, 
        'Academic degree': 6}  
    
    # conditions for the 5 dataset subdivided by education level
    lower_sec = df[df["EDU"] == 'Lower secondary']
    secondary = df[df["EDU"] == 'Secondary / secondary special']
    inc_high = df[df["EDU"] == 'Incomplete higher']
    higher = df[df["EDU"] == 'Higher education']
    academic = df[df["EDU"] == 'Academic degree']

    education_levels = [lower_sec, secondary, inc_high, higher, academic]

    for level in education_levels:
        num_record = level.TARGET.count()
        num_record /= 100
        level["NORM_TARGET"] = level.TARGET / num_record  # normalised 
        print(level.head())

    # Normalization is done in such a fashion that if you sum over the column of 
    # the normalized target you will have exactly the ratio of insolvent/total (%). 
    # This makes possible to make a histogram of arbitrarily wide bins.
    # [e.g. summing over the column of lower_sec will give you 10.93 (%)]
    print(lower_sec.NORM_TARGET.sum())

    fig, axs = plt.subplots(2, 2, figsize = (14, 8))

    sns.histplot(lower_sec, x="AGE", kde=True, ax=axs[0, 0],
                    stat="density", element="step", bins=30, binwidth=1, hue="EDU")
    sns.histplot(secondary, x="AGE", kde=True, ax=axs[0, 1],
                    stat="density", element="step", bins=30, binwidth=1, hue="EDU")
    sns.histplot(inc_high, x="AGE", kde=True, ax=axs[1, 0],
                    stat="density", element="step", bins=30, binwidth=1, hue="EDU")
    sns.histplot(higher, x="AGE", kde=True, ax=axs[1, 1],
                    stat="density", element="step", bins=30, binwidth=1, hue="EDU")
    plt.show()







    
