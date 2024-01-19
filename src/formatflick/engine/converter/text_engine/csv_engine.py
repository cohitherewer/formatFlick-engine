"""
This file contains several functions to read, modify a csv and a tsv file
- read_csv: handles reading the csv or a tsv file
- deflatten_csv: de flatten the csv and tsv file
- deflatten_csv_util: util function for deflatten_csv function
- csv_engine: driver engine to handle all operations for csv and tsv
"""
import csv
import pandas as pd
import src.formatflick.engine.global_var as var


def deflatten_csv_util(d, parent_key='', sep='.'):
    items = {}
    for key, value in d.items():
        keys = key.split(sep)
        curr_level = items
        for k in keys[:-1]:
            curr_level = curr_level.setdefault(k, {})
        curr_level[keys[-1]] = value
    return items


def deflatten_csv(df, sep='.'):
    """
    de flatten the csv file and get the nested structures
    """
    data = []
    for _, row in df.itertools():
        flat_data = row.to_dict()
        nested_data = deflatten_csv_util(flat_data)
        data.append(nested_data)


def read_csv(file_path, delimiter):
    """reading csv file"""
    df = pd.read_csv(file_path, delimiter=delimiter)
    return df


def csv_engine_handle(source, log, *args, **kwargs):
    """
    Handles the csv object as it is
    - read the json object
    - Does flattening of a json object

    Input:
        - source: source csv file
        - log: logger object
    Output:
        - return csv dataframe
    """
    extension = kwargs.get("extension", ".csv")
    log.log_initiating_engine(engine=extension.strip('.'))
    delimiter = ',' if extension == ".csv" else "\t"
    df = read_csv(source, delimiter)
    return df


def csv_engine_convert(destination, obj, log, *args, **kwargs):
    """
    csv convert engine will work in two mode
    - file mode => write the entire resultant data into a file
    - non file mode => return the entire resultant object into a file
    """
    mode = kwargs.get("mode", var.FILE_MODE)
    if mode == var.FILE_MODE:
        sep = kwargs.get("sep", ',')
        extension = kwargs.get("extension", None)
        assert extension is not None

        if isinstance(obj, pd.DataFrame):
            if extension == ".json":
                orient = kwargs.get("orient", "record")
                lines = kwargs.get("lines", True)
                obj.to_json(destination, orient=orient, lines=lines)
            elif extension == ".tsv":
                index = kwargs.get("index", False)
                obj.to_csv(destination, sep=sep, index=index)
            return
        headers = kwargs.get("headers", [])
        newline = kwargs.get("newline", '')
        encoding = kwargs.get("encoding", 'utf-8')

        with open(destination, 'w+', newline=newline, encoding=encoding) as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=sep)
            writer.writeheader()
            writer.writerows(obj)
        return None
    else:
        if isinstance(obj, pd.DataFrame):
            return None
        else:
            # print(type(obj))
            # print(obj)
            assert isinstance(obj, (dict, list)) is True
            df = pd.DataFrame(obj)
            # print(df,"fuck")
            return df
