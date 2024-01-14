# from src.formatflick.engine.Logger_Config import logger as log
import csv
import json
import src.formatflick.engine.converter.utils as utils


class Core_engine:
    """Core_engine that handles the conversion"""

    def __init__(self, source, destination, log):
        self.log = log
        self.log.custom_message(msg="Initiating Process...")
        self.source = source
        self.destination = destination

    def json_to_util(self, *args, **kwargs):
        """
        handle json to csv and tsv file conversion.
        csv and tsv files can be handled in the same way just the delimiter is different
        """
        extension = kwargs.get("extension", None)
        assert extension is not None
        self.log.info(f"Converting from .json to {extension}")
        json_obj = utils.read_json(self.source)
        flatten_json_obj = []
        for item in json_obj:
            flatten_json_obj.append(utils.flatten_json(item))
        headers = list(set(key for entry in flatten_json_obj for key in entry.keys()))
        sep = ',' if extension == ".csv" else '\t'
        with open(self.destination, "w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=sep)
            writer.writeheader()
            writer.writerows(flatten_json_obj)
        self.log.info("Conversion Complete")
        self.log.info(f"Resulting file can be seen at {self.destination}")

    def json_to_csv(self):
        """handles json to csv file conversion"""
        self.json_to_util(extension=".csv")

    def to_json_util(self, extension):
        """handles csv/tsv to json file coversion"""
        self.log.info(f"Converting from {extension} to .json")
        self.log.info(f"Reading the {self.source} file...")
        sep = ',' if extension == ".csv" else '\t'
        data = utils.read_csv(self.source, delimiter=sep)
        self.log.info("Started Conversion...")
        with open(self.destination, 'w+') as json_file:
            json.dump(data, json_file, indent=2)

        self.log.info("Conversion Complete")
        self.log.info(f"Resulting file can be seen at {self.destination}")

    def csv_to_json(self):
        """handles csv to json file conversion"""
        self.to_json_util(extension=".csv")

    def csv_to_tsv(self):
        """handles csv to tsv file conversion"""
        self.log.info("Converting from .csv to .tsv")
        self.log.info(f"Reading the {self.source} file...")

        df = utils.read_csv(self.source)
        df.to_csv(self.destination, sep='\t', index=False)

        self.log.info("Conversion Complete")
        self.log.info(f"Resulting file can be seen at {self.destination}")

    def tsv_to_csv(self):
        """handles tsv to csv file conversion"""
        self.log.info("Converting from .tsv to .csv")
        self.log.info(f"Reading the {self.source} file...")

        df = utils.read_csv(self.source, delimiter='\t')
        df.to_csv(self.destination, index=False)

        self.log.info("Conversion Complete")
        self.log.info(f"Resulting file can be seen at {self.destination}")

    def json_to_tsv(self):
        """handles json to tsv file conversion"""
        self.json_to_util(extension=".tsv")

    def tsv_to_json(self):
        """handles tsv to json file conversion"""
        self.to_json_util(extension=".tsv")

    def custom_convert(self):
        """this function can be overwritten for custom implementations"""
        pass
