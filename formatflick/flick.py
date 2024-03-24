from pathlib import Path
import os

from global_var import *
import logger as log


class flick:
    def __init__(self,
                 source: Path,
                 destination: Path = None,
                 destination_extension: str = None,
                 verbosity: int = None,
                 *args, **kwargs
                 ):
        self.source: Path = source
        self.source_extension: str = ""
        self.destination: Path = destination
        self.destination_extension: str = destination_extension
        self.verbosity: int = verbosity

        self.mode = kwargs.get("mode", None)
        self.log = log.logger(verbosity)

    @staticmethod
    def get_file_extension(file_path: Path) -> str:
        """
        Static method to find out the extension of the given file
        Input:
        - valid file_path
        Output:
        - extensions
        """
        _, extension = os.path.splitext(file_path)
        return extension

    @staticmethod
    def is_valid_file_extension(extension: str) -> bool:
        """
        Static method to find out the extension of the file is valid for the module or not.
        Input:
        - extension
        Output:
        -Boolean value[true/false]
        """
        if extension in VALID_EXTENSIONS:
            raise Exception(
                f"{extension} is not valid. The valid extensions are {VALID_EXTENSIONS}"
            )
        return True

    def is_file_mode(self) -> bool:
        return self.mode == FILE_MODE
    def check_source_validity(self):
        pass

    def check_destination_validity(self):
        pass

    def convert(self):
        pass
