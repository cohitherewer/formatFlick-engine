"""This file is for validation of the source file"""
from formatflick.engine.Logger_Config import logger as log
import os
import formatflick.engine.handler.util as util
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
        log.info("Getting the File Name...")
        u, v = util.get_file_name(self.source)
        if u:
            self.source_file = v
        else:
            log.error(f"Error occurred while extracting File Name: {v}", exc_info=False)
            raise Exception(f"Error while extracting file name from file path {self.source}: {v}")

    def get_extension(self):
        """
        Get the file extension
        """
        log.info("Getting the extension")
        u, v = util.get_extension(self.source_file)
        if u:
            self.extension = v
        else:
            log.error(f"Error occurred while getting File Extension: {v}")
            raise Exception(f"Error while extracting file extension from {self.source_file}: {v}")

    def validate_extension(self):
        """
        Validate the extension
        """
        log.info("Validating the File Extension of Source File")
        if util.validate_extension(self.extension):
            log.info("Valid File Extension")
        else:
            log.error(f"{self.extension} is not a valid File Extension")
            raise Exception(f"{self.extension} is not a valid File Extension")

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
            if u:
                log.info("JSON Encoding Validated")
                self.object = v.copy()
            else:
                log.error("Problem in JSON Encoding")
                raise Exception(f"Problem in JSON Encoding: {v}")

        elif self.extension == ".xml":
            log.infor("Validating the XML Encoding")
            u, v = util.validate_xml(self.source)
            if u:
                log.info("XML Encoding Validated")
                self.object = v.getroot()
            else:
                log.error("Problem in XML Encoding")
                raise Exception(f"Problem in XML Encoding: {v}")

        elif self.extension == ".csv":
            log.info("Skipping the File Validation for CSV")
            self.object = pd.read_csv(self.source)
