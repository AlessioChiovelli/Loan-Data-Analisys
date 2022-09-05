import pandas as pd
import seaborn as sns

def unique_values_of_cols(dataset: pd.DataFrame, columns_to_select: list)-> dict:
    _dict = dict()
    for col in columns:_dict[col] = dataset[col].unique()
    return _dict


def slicing_DF_target_based_on_columns_value(dataset : pd.DataFrame,columns: list, values_of_columns: dict, target_column : str) -> pd.DataFrame:
    """
        Args:
            Columns: Columns we adopt to perform the slicing

        Returns:
            pd.DataFrame: A dataframe containing the values of the     
    """
    df_to_slice = dataset[columns].copy()
    print(df_to_slice)
    
    for col in columns:
        df_to_slice = df_to_slice.loc[df_to_slice[f'{col}'].isin(values_of_columns[col] if type(values_of_columns[col])==list else list(values_of_columns[col]))]
    print(df_to_slice)
    return df_to_slice
    
if __name__ == '__main__':
    dataset = pd.read_csv('/Users/alessio/Desktop/bigdata/data/loan_data.csv')
    columns = ['CODE_GENDER','FLAG_OWN_CAR','CNT_CHILDREN','NAME_EDUCATION_TYPE']
    _dict = unique_values_of_cols(dataset,columns)
    print(_dict)
    _dict['CNT_CHILDREN'] = _dict['CNT_CHILDREN'][:3]
    _dict['FLAG_OWN_CAR'] = _dict['FLAG_OWN_CAR'][0]
    _dict['CODE_GENDER'] = _dict['CODE_GENDER'][0]
    # print(dataset)
    print(_dict)
    
    slicing_DF_target_based_on_columns_value(dataset = dataset, columns = columns, values_of_columns = _dict, target_column = 'TARGET')