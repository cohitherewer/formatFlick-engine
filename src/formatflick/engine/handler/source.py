"""This file is for validation of the source file"""
import os
from .util import *
from ..global_var import *

class SourceFile_handler:
    """
    Handles checks for source files
    Possible Checks are
    - if the file exists in the path or not
    - the file is csv, xml or json or not
    - the file satisfies the encoding or not (specially for json and xml)
    """

    def __init__(self, source, log, *args, **kwargs):
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
        u, v = get_file_name(self.source)
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
        u, v = get_extension(self.source_file)
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
        if validate_extension(self.extension):
            self.log.log_valid_extension_msg()
        else:
            self.log.log_invalid_extension_error(self.extension)
            raise Exception(f"{self.extension} is not a valid File Extension")

    def is_exists(self):
        """
        Validate the source path
        """
        if os.path.exists(self.source):
            self.log.log_custom_message(msg="Path Exists Processing")
        else:
            self.log.log_invalid_file_path(self.source)
            raise FileNotFoundError()

    def validate_file(self):
        if self.extension == JSON:
            self.log.log_validating_file_encoding(self.source)
            u, v = validate_json(self.source)
            if u:
                self.log.log_validated_file_encoding(self.source)
                self.object = v.copy()
            else:
                self.log.log_invalid_file_encoding(self.source)
                raise Exception

        elif self.extension == XML:
            self.log.log_validating_file_encoding(self.source)
            u, v = validate_xml(self.source)
            if u:
                self.log.log_validated_file_encoding(self.source)
                self.object = v.getroot()
            else:
                self.log.log_invalid_extension_error(self.source)
                raise Exception(f"{v}")

        elif self.extension == CSV or self.extension == TSV:
            self.log.log_custom_message(msg=f"Skipping the File Validation for {self.source}")
            # self.object = pd.read_csv(self.source)

        elif self.extension == HTML:
            self.log.log_validating_file_encoding(self.source)
            if validate_html(file_path=self.source):
                self.log.log_validated_file_encoding(self.source)
            else:
                self.log.log_invalid_file_encoding(self.source)

