"""
This module encapsulates a set of functions designed for reading, manipulating,
and deflattening both CSV (Comma-Separated Values) and TSV (Tab-Separated Values) files.
The primary functionalities provided by this module are:

read_csv:
---------
Purpose: This function facilitates the reading of both CSV and TSV files, extracting the data and returning it in a
structured format.
Parameters: The function takes the file path as input and automatically detects the file format (CSV or TSV) based on
the file extension.
Returns: The content of the file is returned in a suitable data structure, such as a list of lists or a pandas
DataFrame.

deflatten_csv:
--------------
Purpose: This function is responsible for de-flattening the contents of CSV and TSV files, which may contain nested
structures or hierarchical data.
Parameters: It accepts the file path of the CSV or TSV file to be deflattened.
Returns: The function processes the input file, resolves any nested structures, and returns a modified version of the
data with flattened hierarchies.

deflatten_csv_util:
-------------------
Purpose: This is a utility function designed to assist the deflatten_csv function in handling the actual de-flattening
process.
Parameters: The utility function takes relevant parameters to support the de-flattening operation within the context of
deflatten_csv.
Returns: It returns intermediate results or modified data structures that contribute to the overall de-flattening
process.

csv_engine:
-----------
Purpose: This function serves as the central driver engine, orchestrating all operations related to CSV and TSV files.
Parameters: It may take parameters related to different operations, such as reading, modifying, or deflattening files.
Returns: Depending on the specific operation requested, this function returns the appropriate output, whether it's the
content of a file, a modified file, or a deflattened version of the data.
The intention of this module is to provide a comprehensive toolkit for working with CSV and TSV files, addressing common
tasks such as reading, modification, and handling hierarchical structures. Users can leverage these functions for
efficient data manipulation and analysis in the context of structured text-based data files.
"""
import csv
import pandas as pd
from ...global_var import *


def deflatten_csv_util(d, parent_key='', sep='.'):
    """
    The deflatten_csv_util function is a utility designed to support the process of de-flattening a nested dictionary
    structure. It takes a flattened dictionary (d) and reconstructs it into a hierarchical or nested format.

    Parameters:

    d(dict): The flattened dictionary to be de-flattened, where keys represent hierarchical levels separated by a
    specified separator.
    parent_key (str, optional): The key representing the parent level during the de-flattening process. Defaults to an
    empty string.
    sep (str, optional): The separator used in the flattened dictionary keys to denote hierarchical levels. Defaults to
    a period ('.').
    Returns:

    dict: The de-flattened dictionary, where nested levels are reconstructed based on the provided separator. Each key
    represents a specific level in the hierarchy, and the corresponding values contain the data associated with that
    level.
    This utility function plays a crucial role in the overall de-flattening process, aiding in the reconstruction of
    hierarchical structures from a flattened representation.
    """
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
    De-flattens the provided DataFrame (`df`) with nested structures, using the specified separator.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing flattened data to be de-flattened.
    - sep (str, optional): The separator used in the flattened DataFrame column names to denote hierarchical levels.
                           Defaults to a period ('.').

    Returns:
    - list: A list of dictionaries, where each dictionary represents a row in the de-flattened DataFrame.
            Nested structures are reconstructed based on the provided separator.

    This function iterates over the rows of the input DataFrame, converts each row to a flattened dictionary,
    and then utilizes the `deflatten_csv_util` utility function to reconstruct nested structures.
    The resulting list contains dictionaries with hierarchical data structures, facilitating easier analysis
    and understanding of nested information within the original flattened DataFrame.
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
    mode = kwargs.get("mode", FILE_MODE)
    if mode == FILE_MODE:
        sep = kwargs.get("sep", ',')
        extension = kwargs.get("extension", None)
        assert extension is not None

        if isinstance(obj, pd.DataFrame):
            if extension == ".json":
                orient = kwargs.get("orient", "records")
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
            assert isinstance(obj, (dict, list)) is True
            df = pd.DataFrame(obj)
            return df
