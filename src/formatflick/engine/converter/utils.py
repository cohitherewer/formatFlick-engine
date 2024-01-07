import json


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
