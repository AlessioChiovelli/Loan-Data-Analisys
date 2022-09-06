import pandas as pd
import seaborn as sns

def unique_values_of_cols(dataset: pd.DataFrame, columns_to_select: list)-> dict:
    _dict = dict()
    for col in columns_to_select:_dict[col] = dataset[col].unique()
    return _dict


def slicing_DF_target_based_on_columns_value(dataset : pd.DataFrame,columns: list, values_of_columns: dict, target_columns : list) -> pd.DataFrame:
    """
        Args:
            Columns: Columns we adopt to perform the slicing

        Returns:
            pd.DataFrame: A dataframe containing the values of the     
    """
    all_columns = columns
    all_columns.extend(target_columns)
    df_to_slice = dataset[all_columns].copy()
    # print(df_to_slice)
    
    for col in columns:
        if col in list(values_of_columns.keys()):
            df_to_slice = df_to_slice.loc[df_to_slice[f'{col}'].isin(values_of_columns[col] if type(values_of_columns[col])==list else list(values_of_columns[col]))]
        else:continue
    # print(df_to_slice[target_columns])
    return df_to_slice[target_columns]
    
if __name__ == '__main__':
    dataset = pd.read_csv('/Users/alessio/Desktop/Big Data/data/loan_data.csv')
    columns = ['CODE_GENDER','FLAG_OWN_CAR','CNT_CHILDREN','NAME_EDUCATION_TYPE']
    _dict = unique_values_of_cols(dataset,columns)
    print(_dict)
    _dict['CNT_CHILDREN'] = _dict['CNT_CHILDREN'][:3]
    _dict['FLAG_OWN_CAR'] = _dict['FLAG_OWN_CAR'][0]
    _dict['CODE_GENDER'] = _dict['CODE_GENDER'][0]
    print(_dict)
    
    df_sliced = slicing_DF_target_based_on_columns_value(dataset = dataset, columns = columns, values_of_columns = _dict, target_columns = ['TARGET'])
    print(df_sliced)