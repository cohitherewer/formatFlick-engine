from typing import Tuple, List, Any
from .engine import engine, dest_engine
import pandas as pd
import xml.etree.ElementTree as ET


class cEngine(engine):
    def __init__(self,
                 source,
                 mode: str,
                 *args, **kwargs
                 ):
        super().__init__(source, mode, args, kwargs)
        self.ext = kwargs.get("source_extension", None)
        if self.ext is None:
            raise Exception("Please give source extension for cEngine")

    def read_file(self) -> Any:
        if self.ext == ".xlsx":
            return pd.read_excel(self.source)
        delimiter = ','
        if self.ext == ".tsv":
            delimiter = '\t'
        return pd.read_csv(self.source, delimiter=delimiter)

    @staticmethod
    def to_json(obj):
        # print("Coming here")
        return obj.to_dict(orient='list')

    @staticmethod
    def to_xml(obj, root=None):
        if root is None:
            root = "Result"
        root = ET.Element(root)
        for i, row in obj.iterrows():
            row_element = ET.SubElement(root, f'{i+1}')
            for col_name, col_value in row.items():
                col_element = ET.SubElement(row_element, col_name)
                col_element.text = str(col_value)
        return ET.tostring(root)


class dest_cEngine(dest_engine):
    def __init__(self, obj, destination, *args, **kwargs):
        super().__init__(obj, destination, args, kwargs)
        self.dest_extension = kwargs.get("destination_extension", None)
        if self.dest_extension is None:
            raise Exception(f"Please destination_extension in dest_cEngine")

    def to_destination(self):
        if self.dest_extension == ".csv":
            self.obj.to_csv(self.destination, index=False, sep=',')
        elif self.dest_extension == ".tsv":
            self.obj.to_csv(self.destination, index=False, sep='\t')
        elif self.dest_extension == ".xlsx":
            self.obj.to_excel(self.destination, index=False)
