"""This file is for validation of the source file"""
# from src.formatflick.engine.Logger_Config import logger as log
import os
from src.formatflick.engine.handler import util
import pandas as pd


class Sourcefile_handler:
    """
    Handles checks for source files
    Possible Checks are
    - if the file exists in the path or not
    - the file is csv, xml or json or not
    - the file satisfies the encoding or not (specially for json and xml)
    """

    def __init__(self, source, log):
        self.source = source
        self.log = log

        self.is_exists()

        self.source_file = None
        self.get_file_name()

        self.extension = None
        self.get_extension()

        self.validate_extension()

        self.object = None
        self.validate_file()

    def get_file_name(self):
        """
        Get the file name
        """
        self.log.log_custom_message(msg="Getting the Source File Name...")
        u, v = util.get_file_name(self.source)
        if u:
            self.source_file = v
        else:
            self.log.log_filename_extraction()
            raise Exception(f"{v}")

    def get_extension(self):
        """
        Get the file extension
        """
        self.log.log_custom_message(msg="Getting the extension...")
        u, v = util.get_extension(self.source_file)
        if u:
            self.extension = v
        else:
            self.log.log_extension_extraction_error()
            raise Exception(f"{v}")

    def validate_extension(self):
        """
        Validate the extension
        """
        self.log.log_extension_extraction_msg(src=self.source_file)
        if util.validate_extension(self.extension):
            self.log.log_valid_extension_msg()
        else:
            self.log.log_invalid_extension_error()
            raise Exception(f"{self.extension} is not a valid File Extension")

    def is_exists(self):
        """
        Validate the source path
        """
        if os.path.exists(self.source):
            self.log.log_custom_message(msg="Path Exists Processing")
        else:
            self.log.log_invalid_file_path()
            raise FileNotFoundError()

    def validate_file(self):
        if self.extension == ".json":
            self.log.log_validating_file_encoding(self.source)
            u, v = util.validate_json(self.source)
            if u:
                self.log.log_validated_file_encoding(self.source)
                self.object = v.copy()
            else:
                self.log.log_invalid_file_encoding(self.source)
                raise Exception

        elif self.extension == ".xml":
            self.log.log_validating_file_encoding(self.source)
            u, v = util.validate_xml(self.source)
            if u:
                self.log.log.validated_file_encoding(self.source)
                self.object = v.getroot()
            else:
                self.log.log_invalid_extension_error(self.source)
                raise Exception(f"{v}")

        elif self.extension == ".csv" or self.extension == ".tsv":
            self.log.log_custom_message(msg=f"Skipping the File Validation for {self.source}")
            self.object = pd.read_csv(self.source)

        elif self.extension == ".html":
            self.log.log_validating_file_encoding(self.source)
