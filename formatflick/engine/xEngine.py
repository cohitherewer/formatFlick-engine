from .engine import engine, dest_engine
from .jEngine import jEngine
from pathlib import Path
# import xml.etree.ElementTree as ET
import xmltodict
import json
import pandas as pd


class xEngine(engine):
    def __init__(self,
                 source: Path,
                 mode: str,
                 *args, **kwargs
                 ):
        super().__init__(source, mode, args, kwargs)

    def read_file(self):
        with open(self.source, "r") as xml_file:
            xml_data = xml_file.readlines()  # returns list of lines
            xml_data = ''.join(xml_data)
            data_dict = xmltodict.parse(xml_data)
        return data_dict

    @staticmethod
    def to_json(obj):
        return json.dumps(obj, indent=4)

    @staticmethod
    def to_csv(obj):
        # need to flatten
        flat_obj = jEngine.flatten_json_util(obj, '_', 0)

        # data = []
        # for key, value in flat_obj.items():
        #     if isinstance(value, list):
        #         for item in value:
        #             data.append(item)
        #     else:
        #         data.append(value)

        # Create DataFrame
        df = pd.DataFrame([flat_obj])
        print(df)
        return df

    @staticmethod
    def to_tsv(obj):
        return xEngine.to_csv(obj)

    @staticmethod
    def to_xlsx(obj):
        return xEngine.to_csv(obj)


class dest_xEngine(dest_engine):
    def __init__(self, obj, destination, *args, **kwargs):
        super().__init__(obj, destination, *args, **kwargs)

    def to_destination(self):
        write_type = "w"
        if type(self.obj) is bytes:
            write_type = "wb"
        with open(self.destination, write_type) as dest:
            dest.write(self.obj)
