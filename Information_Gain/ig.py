import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# libs for Information gain
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_extraction.text import CountVectorizer

sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH, INFORMATION_GAIN_COLUMNS
# @@

def compute_entropy(column: pd.Series) -> float:
    '''Compute entropy for a given Serie.'''
    conta_valori = column.value_counts()
    total = column.count()
    prob_per_class = conta_valori / total  # probability for each class
    log_prob = - np.log2(prob_per_class)
    # print(prob_per_class)
    # print(log_prob)
    entropy = (prob_per_class * log_prob).sum()   # la meno sommatoria di p(xi) * log[p(xi)]
    return entropy

def evaluate():
    df = pd.read_csv(DATASET_PATH)

    entropy_of_target = compute_entropy(df['TARGET'])
    # print(entropy_of_target)

    info_gain_dict = {}
    for column in INFORMATION_GAIN_COLUMNS:

        probabilities = df[["TARGET", column]].groupby(by=column).count() / df[["TARGET", column]].count()['TARGET']
        conditional_entropies = df[["TARGET", column]].groupby(by=column).apply(
                                                        lambda df: compute_entropy(df.TARGET))  # ENTROPIE CONDIZIONATE A X = Xi
        conditional_entropy = (probabilities["TARGET"] * conditional_entropies).sum()

        # Information gain IG(Y|X), hence the information hidden in X about Y, 
        # is the difference of entropy of Y and the conditional entropy of Y given X
        info_gain = entropy_of_target - conditional_entropy  # H(Y) - H(Y|X)
        info_gain_dict[column] = info_gain
        # print(f"Information Gain of column {column} is {info_gain}")



    

    # # toy code in the comment for computation of information gain IG(target|education)
    # # COMPUTATION OF CONDITIONAL ENTROPY:    H(TARGET | EDUCATION)
    # # probabilities = df[["TARGET", "NAME_EDUCATION_TYPE"]].groupby(by="NAME_EDUCATION_TYPE").count() / df[["TARGET", "NAME_EDUCATION_TYPE"]].count()['TARGET']
    
    # # entropie_condizionate = df[["TARGET", "NAME_EDUCATION_TYPE"]].groupby(by="NAME_EDUCATION_TYPE").apply(
    # #                                                 lambda df: compute_entropy(df.TARGET)) # ENTROPIE CONDIZIONATE A X = Xi

    # # entropia_condizionata_totale = (probabilities["TARGET"] * entropie_condizionate).sum()

    # # print(probabilities["TARGET"])
    # # print(entropie_condizionate)
    # # print(entropia_condizionata_totale)

    # # print(entropy_of_target)
    # # print(entropia_condizionata_totale)
    # # print(f"information gain is {entropy_of_target - entropia_condizionata_totale}")



   
        
    

        