import logging

def pretty_print_of_dict(source: dict, file_name: str, type_output: str = "txt", nested_level: int = 0):
    """
    Generate a file on which the dictionary is pretty writted inside
    Args:
        stats_dict (dict): source dictionary
        file_name (str): name of the output file
        type_output (str, optional): type of file output
        nested_level (int, optional): if the dictionary that you wanna print is nested with a certain level of depth
    """
    assert len(file_name) > 0
    logging.info(f"@@ METHOD CALL: pretty_print_of_dict\n")
    logging.info(f"@@@ Parameters:\n source: {source},\n file_name: {file_name}\n")
    with open(f'{file_name}.{type_output}', 'w' if nested_level == 0 else 'a') as f:
        print(nested_level*"\t"+30*'*', file = f)
        for _key, _value in source.items():
            nested_level = 0
            if isinstance(_value, dict):
                nested_level += 1
                print(f'{_key}', file = f)
                for __key, __value in _value.items():
                    print(nested_level*"\t"+f'{__key} : {__value}', file = f)
                print("\n")
            else:
                print(nested_level*"\t"+f'{_key} : {_value}', file = f)