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


    # # Prepare plot
    # figure, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 5))
    # figure.suptitle('Education distribution')
    # axes[0].set_title('Gender: Male')
    # axes[1].set_title('Gender: Female')
    # axes[2].set_title('General View')
    # #
    
    # # Make subplot for male distribution
    # sns.histplot(df[edu].value_counts(), ax = axes[0], x = edu, kde = True, stat = "density", element = "step", bins = 100, binwidth = 1)

    

    



if __name__ == "__main__":
    evaluate()