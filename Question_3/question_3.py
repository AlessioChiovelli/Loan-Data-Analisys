import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # @@ Personal Libraries
# from CONFIG import DATASET_PATH
# from Utils.Statistics.Dataframe.slicing import *
# # @@

sns.set()  # Set style as seaborn even with 

def evaluate():
    """Evaluate the question, and try to give an answer.
    """
    dataset = pd.read_csv("data/loan_data.csv")

    # Add age on the dataset
    # Estimate age of birth, given every month of 31d and all years of 365d
    dataset["APPROX_AGE"] = (dataset["DAYS_BIRTH"] /
                                365).apply(lambda element: abs(int(element)))
    dataset["APPROX_YEAR_REGISTRATION"] = (dataset["DAYS_REGISTRATION"] /
                                365).apply(lambda element: abs(int(element)))
    sns.histplot(data=dataset,x="APPROX_AGE",kde=True,binwidth=1, stat = "probability")
    plt.show()
    # Plot the responses for different events and regions
    sns.jointplot(data=dataset,x="APPROX_AGE", y="APPROX_YEAR_REGISTRATION", kind="hex", color="#4CB391")
    plt.show()
    
if __name__ == '__main__':
    evaluate()