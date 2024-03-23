"""
This module encapsulates a set of functions desined for reading, manipulating,
and deflattening XLSX(Microsoft Excel files) files.

read_excel:
----------
Purpose: This function facilitates the reading of excel file, extracting the data in structured format
Parameters: The function takes the file path as input and automatically detects the file extension
Returns:
    The content of the file is returned in a suitable data structure
"""

import openpyxl as xl
import pandas as pd

from formatflick.global_var import *


def read_excel(file_path, **kwargs):
    """reading the Excel file"""
    try:
        wb = xl.load_workbook(filename=file_path)
        return True, wb
    except Exception as err:
        return False, err


def xlsx_engine_handle(source, log, *args, **kwargs):
    """
    Handles the Excel object as it is
    -
    """
    print("coming here")
    extension = kwargs.get("extension", None)
    assert extension is not None
    log.log_initiating_engine(engine=extension.strip('.'))
    df = read_excel(source, kwargs=kwargs)
    print("Magi", df)
    return df


def xlsx_engine_convert(destination, obj, log, *args, **kwargs):
    """
    Excel convert engine will work in two modes
    - file mode => write the entire resultant data into a file
    - non file mode => return the entire resultant object inta a suitable object
    """
    mode = kwargs.get("mode", FILE_MODE)
    if mode == FILE_MODE:
        if isinstance(obj, pd.DataFrame):
            extension = kwargs.get("extension", None)
            assert extension is not None
            if extension == ".json":
                orient = kwargs.get("orient", "recods")
                lines = kwargs.get("lines", True)
                obj.to_excel(destination, orient=orient, lines=lines)
            elif extension == ".tsv" or extension == ".csv":
                index = kwargs.get("index", False)
                obj.to_csv(destination, index=index)
            return

        headers = kwargs.get("headers", [])
        newline = kwargs.get("newline", [])
        encoding = kwargs.get("encoding", 'utf-8')

        wb = xl.Workbook()
        ws = wb.active
