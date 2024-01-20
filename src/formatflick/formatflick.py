"""Main module for Formatflick"""
from .engine.handler import source as src
from .engine.handler import destination as dst
from .engine.converter import core
from .engine.Logger_Config import create_logger
from .engine.global_var import *
import time


class formatflick:
    """
    Initializes an instance of the formatflick class with the provided source and destination paths.
    Parameters:
    - source (str): The source path for the module.
    - destination (str, optional): The destination path for the operation.
        If not provided, the current working directory is used.
    - *args: Additional positional arguments.
    - **kwargs: Additional keyword arguments.
    """

    def __init__(self, source, destination=None, *args, **kwargs):
        """init"""
        self.mode = kwargs.get("mode", FILE_MODE)
        self.source = source
        self.destination = destination
        self.destination_extension = kwargs.get("destination_extension", None)

        verb = kwargs.get("verbosity", 3)
        self.log = create_logger(verb)
        self.source_obj = src.SourceFile_handler(source=self.source, log=self.log, args=args, kwargs=kwargs)

        # mode = kwargs.get("mode", var.FILE_MODE)
        self.dst_obj = dst.DestinationFile_handler(destination=self.destination,
                                                   dst_extension=self.destination_extension,
                                                   log=self.log,
                                                   mode=self.mode
                                                   )
        if self.mode == FILE_MODE:
            self.engine = core.Core_engine(source=self.source_obj.source,
                                           destination=self.dst_obj.destination,
                                           log=self.log,
                                           mode=self.mode
                                           )
        else:
            self.engine = core.Core_engine(source=self.source_obj.source,
                                           log=self.log,
                                           extension=self.dst_obj.extension,
                                           mode=self.mode
                                           )
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
        conversion_key = (self.source_obj.extension, self.dst_obj.extension)
        res = None
        if conversion_key in self.function_call_map:
            conversion_function = self.function_call_map[conversion_key]
            res = conversion_function()
        else:
            self.log.log_unsupported_file_conversion_error(self.source_obj.extension, self.dst_obj.extension)
        end_time = time.time()
        self.log.log_time(end_time, start_time)
        return res
