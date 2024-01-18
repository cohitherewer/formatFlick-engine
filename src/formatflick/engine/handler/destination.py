import os
from src.formatflick.engine.handler import util
# from src.formatflick.engine.Logger_Config import logger as self.log


class DestinationFile_handler:
    """
    Handles checks for destination files
    Possible Checks are
    - if the file exists in the path or not
        - if it does not exist raise exception
    - the file is csv, xml or json or not
    """

    def __init__(self, destination, dest_extension, log, *args, **kwargs):
        self.log = log

        if not (destination or dest_extension):
            raise Exception("Either destination or destination_extension should be given.")
        self.destination = destination if destination is not None else (
            os.path.join(os.getcwd(), 'result' + dest_extension))
        self.destination_file = destination if destination is not None else 'result'+dest_extension
        self.extension = self.get_extension()
        self.validate_extension()

    def validate_extension(self):
        """validate the extension"""
        self.log.log_extension_extraction_msg(src=self.destination)
        if util.validate_extension(self.extension):
            self.log.log_valid_extension_msg()
        else:
            self.log.log_invalid_extension_error(self.extension)
            raise Exception(f"{self.extension} is not a valid File Extension")

    def get_extension(self):
        """Get the extension"""
        self.log.log_custom_message(msg="Getting the Destination File Extension")
        u, v = util.get_extension(self.destination_file)
        if u:
            return v
        else:
            self.log.log_extension_extraction_error()
            raise Exception(f"{v}")

    def create_dest_file(self):
        """Creating the destination file"""
        self.log.custom_message(msg="Creating the destination file...")
        if os.path.exists(self.destination):
            self.log.log_path_exists_warning()
        else:
            self.log.log_custom_message(f"Creating a file with path: {self.destination_file}")
            u, v = util.create_file(self.destination)
            if u:
                self.log.log_create_file()
            else:
                self.log.log_create_file_error()
                raise Exception(f"{v}")
