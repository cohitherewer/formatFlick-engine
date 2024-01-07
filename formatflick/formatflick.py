"""Main module for Formatflick"""
import os
from formatflick.engine.handler import source as src
from formatflick.engine.handler import destination as dest
from formatflick.engine.converter import core
from formatflick.engine.Logger_Config import logger as log
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
        self.source_obj = src.Sourcefile_handler(self.source)
        self.dest_obj = dest.DestinationFile_handler(self.destination, self.destination_extension)

    def convert(self):
        """
        Convert method for the module

        Parameters:
        """
        start_time = time.time()
        engine = core.Core_engine(self.source_obj.source,self.dest_obj.destination)
        # print(self.source_obj)
        # print(self.dest_obj)
        if self.source_obj.extension == ".json" and self.dest_obj.extension == ".csv":
            engine.json_to_csv()

        end_time = time.time()
        log.info(f"Time Taken: {end_time-start_time}s")
