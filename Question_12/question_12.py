
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# TODO complete the comment on seaborn style
sns.set()  # Set style as seaborn even with 

# @@ Personal Libraries
from CONFIG import DATASET_PATH
# @@
def evaluate():
    """Evaluate the question, and try to give an answer.
    """    
    dataset = pd.read_csv(DATASET_PATH)

    # # Prepare plot
    ratio=dataset.groupby(["NAME_FAMILY_STATUS","CNT_CHILDREN","FLAG_OWN_CAR"]).apply(lambda group: group.TARGET.sum()/group.shape[0])
    ratio = ratio.reset_index()
    # sns.histplot(data=ratio, x="CNT_CHILDREN", y=ratio[0].values.tolist(), hue="NAME_FAMILY_STATUS",stat="density",kde=True)
    # # sns.histplot(data=dataset, x="NAME_FAMILY_STATUS",discrete=(True, True), y="CNT_CHILDREN", hue="FLAG_OWN_CAR",stat="density",kde=True)
    # plt.show()
    import plotly.express as px
    import pandas as pd
    import numpy as np
    # Read data from a csv
    ratio["FLAG_OWN_CAR"] = ratio["FLAG_OWN_CAR"].apply(lambda element: 1 if element == "Y" else 0)
    _unique_values_family_status: np.array = ratio["NAME_FAMILY_STATUS"].unique()
    _family_status_temp_dict = dict(zip(_unique_values_family_status,range(len(_unique_values_family_status))))
    ratio["NAME_FAMILY_STATUS"] = ratio["NAME_FAMILY_STATUS"].apply(lambda element: _family_status_temp_dict[element])
    fig = px.scatter_3d(x=ratio['CNT_CHILDREN'].values, y=ratio['NAME_FAMILY_STATUS'].values, z=ratio[0].values, symbol=ratio['NAME_FAMILY_STATUS'].values, color=ratio['FLAG_OWN_CAR'].values)
    fig.show()