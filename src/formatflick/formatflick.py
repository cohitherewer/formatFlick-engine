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

    def __init__(self, source, destination=None,
                 destination_extension=None,
                 *args, **kwargs):
        """
        Initialises as instance of formatflick class with the provided source and some optional parameters:
        Right now this module operates two modes => 'file' and 'nfile'
        - 'file' mode will produce a destination file (which will may or may nor be provided by user)
        - 'nfile' mode will produce a destination object (which should be provided by the user)

        Inputs are as follows (an Extensive list)
        1. source: source file path. Ensure that you have entered path in accordance to the os
        2. destination:
            By default, it is set as None
        3. destination_extension:
            By default, it is set as None
            Remember to you have to put the number in such a way that module should be able to extract the extention to which you want to conver
            You either have to provide destination or destination extention.
            Below are some combinations of destination and destination_extension that will work,
                - destination = None and destination_extension = <dot> <any valid extension>
                - destination = <file path with a valid extension> and destination_extension (will be ignored)
        4. mode:
            There are two file modes for formatflick module(optional field)
            The value of mode is set to 'file' mode
                - 'file' outputs the resultant data into destination file
                - 'nfile' outputs the resultant data into destination file and also returns a dataframe
        5. verbosity:
            verbosity defines the level of logging user want while executing the module.
            The values are consistent with the python logging module;
            By default, it is set to 3
        """
        self.mode = kwargs.get("mode", FILE_MODE)
        self.source = source
        self.destination = destination
        self.destination_extension = destination_extension

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
            #  source file is json
            (".json", ".csv"): self.engine.json_to_csv,
            (".json", ".tsv"): self.engine.json_to_tsv,
            (".json", ".html"): self.engine.json_to_html,
            # source file is .csv
            (".csv", ".json"): self.engine.csv_to_json,
            (".csv", ".tsv"): self.engine.csv_to_tsv,
            (".csv", ".html"): self.engine.csv_to_html,
            # source file is .tsv
            (".tsv", ".csv"): self.engine.tsv_to_csv,
            (".tsv", ".json"): self.engine.tsv_to_json,
            (".tsv", ".html"): self.engine.tsv_to_html,
            # source file is .html
            (".html", ".csv"): self.engine.html_to_csv,
            (".html", ".json"): self.engine.html_to_json,
            (".html", ".tsv"): self.engine.html_to_tsv,
        }

    def convert(self):
        """
        convert method for formatflick. This method can only be called once the __init__method is called
        successfully. The __init__method will check all valid file formats, encoding etc. Convert method will call the
        engine and convert from source file to destination file, optionally returning the destination object as well.

        There is an important check the convert does. During initialization, the source and destination file
        validation is done Right now all file formats the formal flick support can be converted between each other,
        But there might possibility where all formats cannot be connected to other formats. To prevent that,
        we add an extra checks where all valid conversions will be mentioned In that it will be helpful to prevent an
        unwanted result and users can don't need to debug that yourselves.
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
