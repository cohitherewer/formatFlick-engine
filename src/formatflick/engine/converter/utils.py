import json
import pandas as pd


def flatten_json_util(json_obj, prefix):
    flat_dict = {}
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_key = f"{prefix}{key}."
            flat_dict.update(flatten_json_util(value, new_key))
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            new_key = f"{prefix}{i}."
            flat_dict.update(flatten_json_util(item, new_key))
    else:
        flat_dict[prefix[:-1]] = json_obj  # Remove the trailing dot
    return flat_dict


def flatten_json(json_object):
    return flatten_json_util(json_object, prefix='_')


def read_json(file_path):
    """Reading a json file"""
    with open(file_path, "r") as file:
        obj = json.load(file)
    return obj


def read_csv(file_path):
    """Reading csv file"""
    df = pd.read_csv(file_path)
    return df


def flat_to_nested(d, parent_key='', sep='.'):
    items = {}
    for key, value in d.items():
        keys = key.split(sep)
        curr_level = items
        for k in keys[:-1]:
            curr_level = curr_level.setdefault(k, {})
        curr_level[keys[-1]] = value
    return items


def deflatten_csv_util(df, sep='.'):
    """de flatten the csv file and get the nested structures"""
    data = []
    for _, row in df.iterrows():
        flat_data = row.to_dict()
        nested_data = flat_to_nested(flat_data)
        data.append(nested_data)
    return data
