import os
from .util import *


class DestinationFile_handler:
    """
    Handles checks for destination files
    Possible Checks are
    - If the file exists in the path or not
        - if it does not exist raise exception
    - the file is csv, xml or json or not
    """
    def __init__(self, destination, dst_extension, log, *args, **kwargs):
        # print(kwargs)
        self.mode = kwargs.get("mode", "file")
        self.log = log
        if self.mode == "file":
            if not (destination or dst_extension):
                raise Exception("Either destination or destination_extension should be given.")
            self.destination = destination if destination is not None else (
                os.path.join(os.getcwd(), 'result' + dst_extension))
            self.destination_file = destination if destination is not None else 'result'+dst_extension
            self.extension = self.get_extension()
            self.validate_extension()
        else:
            if dst_extension is None:
                raise Exception("destination_extension should be provided if the mode is not 'file'")
            self.extension = dst_extension
            self.validate_extension()

    def validate_extension(self):
        """validate the extension"""
        try:
            self.log.log_extension_extraction_msg(src=self.destination)
        except AttributeError:
            pass
        if validate_extension(self.extension):
            self.log.log_valid_extension_msg()
        else:
            self.log.log_invalid_extension_error(self.extension)
            raise Exception(f"{self.extension} is not a valid File Extension")

    def get_extension(self):
        """Get the extension"""
        self.log.log_custom_message(msg="Getting the Destination File Extension")
        u, v = get_extension(self.destination_file)
        if u:
            return v
        else:
            self.log.log_extension_extraction_error()
            raise Exception(f"{v}")
