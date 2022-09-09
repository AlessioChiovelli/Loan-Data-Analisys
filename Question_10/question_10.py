import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH


def evaluate():
    df = pd.read_csv(DATASET_PATH)
    edu, target, children = "NAME_EDUCATION_TYPE", "TARGET", "CNT_CHILDREN"  

    df = df[[edu, children, target]]
    df.rename(columns={"CNT_CHILDREN": "CHILDREN", 
        "NAME_EDUCATION_TYPE": "EDU"}, inplace=True)


    rates = df.loc[df.CHILDREN <= 5].groupby(by=["EDU", "CHILDREN"]).mean() * 100
    print(rates)
    # print(rates.index)  # we have a multi-index object, I want to separate for academic stuff
    
    ax = rates.unstack(level=0).plot(kind='bar', subplots=True, rot=0, figsize=(10, 6), layout=(2, 3),
        title="Insolvency Rates with respect to Education Level and Number of Children", legend=False)
        # TODO non riesco a mettere il label all'asse y
    #ax.set_ylabel = ["%", "%", "%", "%", "%"]  # non funziona perché ax è un oggetto numpy.ndarray 
    print(type(ax))

    plt.tight_layout()
    plt.show()
