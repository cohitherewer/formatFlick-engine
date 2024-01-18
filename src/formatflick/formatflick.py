"""Main module for Formatflick"""
from src.formatflick.engine.handler import source as src
from src.formatflick.engine.handler import destination as dest
from src.formatflick.engine.converter import core
from src.formatflick.engine.Logger_Config import create_logger
import time


class Formatflick:
    """
    Initializes an instance of the Formatflick class with the provided source and destination paths.

    Parameters:
    - source (str): The source path for the module.
    - destination (str, optional): The destination path for the operation.
        If not provided, the current working directory is used.
    - *args: Additional positional arguments.
    - **kwargs: Additional keyword arguments.
    """

    def __init__(self, source, destination=None, *args, **kwargs):
        """init"""
        self.source = source
        self.destination = destination
        self.destination_extension = kwargs.get("destination_extension", None)

        verb = kwargs.get("verbosity", 3)
        self.log = create_logger(verb)
        self.source_obj = src.Sourcefile_handler(self.source, self.log)
        self.dest_obj = dest.DestinationFile_handler(self.destination, self.destination_extension, self.log)

        self.engine = core.Core_engine(self.source_obj.source, self.dest_obj.destination, self.log)
        self.function_call_map = {
            (".json", ".csv"): self.engine.json_to_csv,
            (".csv", ".json"): self.engine.csv_to_json,
            (".csv", ".tsv"): self.engine.csv_to_tsv,
            (".tsv", ".csv"): self.engine.tsv_to_csv,
            (".tsv", ".json"): self.engine.tsv_to_json,
            (".json", ".tsv"): self.engine.json_to_tsv
        }

    def convert(self):
        """
        Convert method for the module
        Parameters:
        """
        start_time = time.time()
        conversion_key = (self.source_obj.extension, self.dest_obj.extension)
        if conversion_key in self.function_call_map:
            conversion_function = self.function_call_map[conversion_key]
            conversion_function()
        else:
            self.log.log_unsupported_file_conversion_error(self.source_obj.extension, self.dest_obj.extension)
        end_time = time.time()
        self.log.log_time(end_time, start_time)
