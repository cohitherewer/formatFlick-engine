import formatflick.engine.converter.utils as utils
from formatflick.engine.Logger_Config import logger as log
import csv


class Core_engine:
    """Core_engine that handles the conversion"""

    def __init__(self, source, destination):
        log.info("Initiating Conversion")
        self.source = source
        self.destination = destination

    def json_to_csv(self):
        log.info("Converting from JSON to CSV")
        json_obj = utils.read_json(self.source)
        flatten_json_obj = []
        for item in json_obj:
            flatten_json_obj.append(utils.flatten_json(item))

        headers = list(set(key for entry in flatten_json_obj for key in entry.keys()))
        print(self.destination)
        with open(self.destination, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(flatten_json_obj)
        log.info("Conversion Complete")
        log.info(f"Resulting file can be seen at {self.destination}")
