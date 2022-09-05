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

    # Add age on the dataset
    # Estimate age of birth, given every month of 31d and all years of 365d
    dataset["APPROX_AGE"] = (dataset["DAYS_BIRTH"] /
                                31/12).apply(lambda element: abs(int(element)))

    # Filter male and female from dataset
    male_payer = dataset["CODE_GENDER"] == "M"
    female_payer = dataset["CODE_GENDER"] == "F"
    ###

    # Prepare plot
    figure, axes = plt.subplots(3, 1, sharex=True, figsize=(10, 5))
    figure.suptitle('Age distribution wrt SEX')
    axes[0].set_title('Gender: Male')
    axes[1].set_title('Gender: Female')
    axes[2].set_title('General View')
    #
    
    # Make subplot for male distribution
    sns.histplot(dataset[male_payer], ax=axes[0], x="APPROX_AGE", kde=True,
                    stat="density", element="step", bins=100, binwidth=1, hue="CODE_GENDER")
    axes[0].set_xticks(dataset[male_payer].groupby("APPROX_AGE").apply(
        lambda group: group.iloc[0].APPROX_AGE).tolist())
    #
    
    # Make subplot for female distribution
    sns.histplot(dataset[female_payer], ax=axes[1], x="APPROX_AGE", kde=True,
                    stat="density", element="step", bins=100, binwidth=1, hue="CODE_GENDER")
    axes[1].set_xticks(dataset[female_payer].groupby("APPROX_AGE").apply(
        lambda group: group.iloc[0].APPROX_AGE).tolist())
    #
    
    # Make subplot for binary distribution of both male and female 
    sns.histplot(dataset[(dataset["CODE_GENDER"] == "M") | (dataset["CODE_GENDER"] == "F")], ax=axes[2],
                    x="APPROX_AGE", kde=True, stat="density", element="step", bins=100, binwidth=1, hue="CODE_GENDER")
    axes[2].set_xticks(dataset[(dataset["CODE_GENDER"] == "M") | (dataset["CODE_GENDER"] == "F")].groupby(
        "APPROX_AGE").apply(lambda group: group.iloc[0].APPROX_AGE).tolist())
    #
    
    plt.show()