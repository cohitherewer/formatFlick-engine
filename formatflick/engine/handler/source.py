"""This file is for validation of the source file"""
from formatflick.engine.Logger_Config import logger as log
import os
import util
import pandas as pd


class Sourcefile_handler:
    """
    Handles checks for source files
    Possible Checks are
    - if the file exists in the path or not
    - the file is csv, xml or json or not
    - the file satisfies the encoding or not ( specially for json and xml)
    """

    def __init__(self, source):
        self.source = source
        self.is_exists()
        self.source_file = self.get_file_name()
        self.extension = self.get_extension()

        self.valid_extension = [".xml", ".csv", ".json"]
        self.validate_extension()

        self.object = None
        self.validate_file()

    def get_file_name(self):
        """
        Get the file name
        """
        log.info("Getting the File Name...")
        try:
            return os.path.basename(self.source)
        except Exception as err:
            log.error(f"Error occurred while extracting File Name: {err}")

    def get_extension(self):
        """
        Get the file extension
        """
        log.info("Getting the extension")
        try:
            return os.path.splitext(self.source_file)[1]
        except Exception as err:
            log.error(f"Error occurred while getting File Extension: {err}")

    def validate_extension(self):
        """
        Validate the extension
        """
        log.info("Validating the File Extention")
        if self.extension in self.valid_extension:
            log.info("Valid File Extension")
        else:
            log.error(f"{self.extension} is not a valid File Extension")

    def is_exists(self):
        """
        Validate the source path
        """
        if os.path.exists(self.source):
            log.info("Path Exists Processing ...")
        else:
            log.error(f"The file at {self.source} doesn't exist")
            raise FileNotFoundError(f"The file at {self.source} doesn't exist")

    def validate_file(self):
        if self.extension == ".json":
            log.info("Validating the JSON Encoding...")
            u, v = util.validate_json(self.source)
            if u is True:
                log.info("JSON Encoding Validated")
                self.object = v.copy()
            else:
                log.error("Problem in JSON Encoding")
                raise Exception(f"Problem in JSON Encoding: {v}")
        elif self.extension == ".xml":
            pass
        elif self.extension == ".csv":
            log.info("Skipping the File Validation for CSV")
            self.object = pd.read_csv(self.source)
