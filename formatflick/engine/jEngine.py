from typing import Tuple, List, Any

from .engine import engine, dest_engine
from pathlib import Path
import json
import pandas as pd
import xml.etree.ElementTree as ET


class jEngine(engine):
    def __init__(self,
                 source: Path,
                 mode: str,
                 *args, **kwargs
                 ):
        super().__init__(source, mode, args, kwargs)

    def read_file(self) -> tuple[list[Any], list[Any]]:
        """
        Reading the JSON file.
        We are using json module of python to read the data.
        Upon reading we are flattening the data json object.
        That will be easier to handle
        While returning we are returning the headers and flatten_object all together
        """
        with open(self.source) as json_file:
            obj = json.load(json_file)
        flatten_obj = []
        for item in obj:
            flatten_obj.append(flatten_obj(item))
        headers = list(set(key for entry in flatten_obj for key in entry.keys()))
        return headers, flatten_obj

    @staticmethod
    def flatten_json_util(json_obj, prefix):
        flat_dict = {}
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                _key = f"{prefix}{key}"
                flat_dict.update(jEngine.flatten_json_util(value, _key))
        elif isinstance(json_obj, list):
            for i, item in enumerate(json_obj):
                _key = f"{prefix}{i}"
                flat_dict.update(jEngine.flatten_json_util(item, _key))
        else:
            flat_dict[prefix[:-1]] = json_obj
        return flat_dict

    def flatten_json(self, json_obj):
        """
        Flatten method for json objects
        """
        prefix = self.kwargs.get("prefix", '_')
        return self.flatten_json_util(json_obj, prefix)

    @staticmethod
    def to_csv(obj):
        """
        Static method to convert a json object into csv(pandas dataframe)
        """
        return pd.DataFrame(obj)

    @staticmethod
    def to_tsv(obj):
        """
        Static method to convert a json object into tsv(pandas dataframe)
        """
        return jEngine.to_csv(obj)

    @staticmethod
    def to_xlsx(obj):
        """
        Static method to convert a json object into xlsx(pandas dataframe)
        """
        return jEngine.to_csv(obj)

    @staticmethod
    def to_xml(obj, root=None):
        """
        Static method to convert a json object into xml format(xml dataframe). Needs testing
        """
        if root is None:
            root = "Result"
        root = ET.Element(root)
        for item in obj:
            for key, value in item.items():
                sub_element = ET.SubElement(root, key)
                sub_element.text = str(value)
        return ET.tostring(root)


class dest_jEngine(dest_engine):
    def __init__(self, obj, destination, *args, **kwargs):
        super().__init__(obj, destination, *args, kwargs)

    def to_destination(self):
        """
        Will get a json object and convert that to a destination file
        """
        with open(self.destination, 'w') as dest:
            json.dump(self.obj, dest)

