"""
This file contains all necessary functions to modify a json object
- read_json: handles reading the json
- flatten_json: handles flattening of the json
- flatten_json_util: utility function for handling the flattening of json
- json_engine: handles all these things together
"""

import json
import src.formatflick.engine.global_var as var


def read_json(file_path):
    """Reading a json file"""
    with open(file_path, "r") as file:
        obj = json.load(file)
    return obj


def flatten_json_util(json_obj, prefix='_'):
    """
    utility function
    - Input:
        - json_obj: mandatory field
        - prefix: optional field, default is set to '_'
    -Output:
        return flatten json object
    """
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


def flatten_json(json_object, *args, **kwargs):
    """
    flatten the json object
    Input:
        - json_object: mandatory field
        - *args:
        - **kwargs: optionally expects prefix field
    Output:
        - return flatten json_object
    """
    prefix = kwargs.get("prefix", '_')
    return flatten_json_util(json_object, prefix=prefix)


def json_engine_handle(source, log, *args, **kwargs):
    """
    Handles the json object as it is.
    - read the json object
    - Does flattening of a json object

    Input:
        - source: source json file
        - log: logger object
    Output:
        - return flat json object and corresponding headers
    """
    log.log_initiating_engine(engine="json")
    obj = read_json(source)
    # mode = kwargs.get("mode", "file")
    flatten_obj = []
    for item in obj:
        flatten_obj.append(flatten_json(item))
    headers = list(set(key for entry in flatten_obj for key in entry.keys()))
    return flatten_obj, headers


def json_engine_convert(destination, log, data, *args, **kwargs):
    """
    Handles conversion of any incoming dataframe or object into json
    Input:
        - destination: destination file
        - log: log object to print the logs
        - data: incoming object
        - args: optional
        - kwargs: optional. Optionally expect indent parameter
    """
    mode = kwargs.get("mode", var.FILE_MODE)
    data = data.to_json()  # added as dataframe is not json serializable
    if mode != var.FILE_MODE:
        return data
    indent = kwargs.get("indent", 2)
    with open(destination, 'w+') as file:
        json.dump(data, file, indent=indent)
