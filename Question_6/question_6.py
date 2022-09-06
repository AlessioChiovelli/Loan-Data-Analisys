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
    df = pd.read_csv(DATASET_PATH)
    edu, target = "NAME_EDUCATION_TYPE", "TARGET"

    # print(df[edu].unique()) # there are 5 different types of educations
    # order is partly based on the ISCED level scale, 
    # the higher the value, the higher the education level
    edu_levels = {
        'Secondary / secondary special': 3, 
        'Higher education': 5, 
        'Incomplete higher': 4, 
        'Lower secondary': 2, 
        'Academic degree': 6}  

    # for k,v in df[edu].value_counts().items():
    #     print(f"{k}: {v}")

    temp = df[edu].value_counts()

    # preparing data for plotting
    edu_labels = list(temp.keys())
    slices = list(temp)
    # explode = [0, 0, 0, 0, .15]  # if you wanna pull a slice from the center, uncomment this

    # prepare plotting
    colors = ["#004c6d","#3c6b88", # color palette found on https://www.learnui.design/tools/data-color-picker.html 
            "#658ca4", "#8eaec1",
            "#b8d2e0", "#e4f6ff" ]

    plt.title("Number of People by Education Level")
    plt.pie(slices, labels = edu_labels, # explode = explode, 
        colors = colors[1:], wedgeprops = {"edgecolor": "black"})
    plt.tight_layout(pad = .8)
    plt.show()





    # small_df = df[[target, edu]]
    # print(small_df[df.TARGET == 1].count() * 100 / small_df[target].count())
    # total = small_df.count()

    # ord_edu_labels = ['Lower secondary', 'Secondary / secondary special', 
    #     'Incomplete higher', 'Higher education', 'Academic degree']  # ordered by level

    # ratios = {}
    # # counting for each type of education levels the ratio between the positive TARGET and the total number of TARGET
    # for edu_type in ord_edu_labels:
    #     temp_df = small_df[small_df.NAME_EDUCATION_TYPE == edu_type]
    #     ratios[edu_type] = round((100 * temp_df[temp_df.TARGET == 1].count()/ temp_df.count()), 2)
    
    # ratios = pd.DataFrame(ratios)
    # print(ratios)

    # ratios.plot.bar()

    # plt.style.use("fivethirtyeight")
    # plt.title("Rate of Target Positivity by Education Level")
    # plt.xlabel("Education")
    # plt.ylabel("Rate of Insolvency (%)")

    # plt.tight_layout()
    # plt.show()

    small_df_0 = df[[target, edu]].loc[df.TARGET == 0]
    small_df_1 = df[[target, edu]].loc[df.TARGET == 1]
    
    group0 = small_df_0.groupby(by=edu)
    group1 = small_df_1.groupby(by=edu)


    print(100 * group1.size()/group0.size())
    print(group1.size())
    
    '''
        sort_values(ascending=False)'''