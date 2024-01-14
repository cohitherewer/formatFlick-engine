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

    def __init__(self, destination, dest_extension, log):
        self.log = log

        if not (destination or dest_extension):
            raise Exception("Either destination or destination_extension should be given.")
        self.destination = destination if destination is not None else (
            os.path.join(os.getcwd(), 'result' + dest_extension))
        self.destination_file = destination if destination is not None else 'result'
        self.extension = dest_extension if dest_extension is not None else self.get_extension()
        self.validate_extension()

    def validate_extension(self):
        """validate the extension"""
        self.log.info("Validating File Extension of Destination File")
        if util.validate_extension(self.extension):
            self.log.info("Valid File Extension")
        else:
            self.log.error(f"{self.extension} is not a valid File Extension")
            raise Exception(f"{self.extension} is not a valid File Extension")

    def get_extension(self):
        """Get the extension"""
        self.log.info("Getting the Extension")
        u, v = util.get_extension(self.destination_file)
        if u:
            self.log.debug(f"Destination File Extension is {v}")
            return v
        else:
            self.log.error(f"Error occurred while getting File Extension: {v}")
            raise Exception(f"Error while extracting file extension from {self.destination_file}: {v}")

    def create_dest_file(self):
        """Creating the destination file"""
        self.log.info("Creating the destination file...")
        if os.path.exists(self.destination):
            self.log.warn(f"Path: {self.destination} already exists")
        else:
            self.log.info(f"Creating a file with path:{self.destination_file}")
            u, v = util.create_file(self.destination)
            if u:
                self.log.info("Destination File Created Successfully")
            else:
                self.log.error("Error in creating Destination File")
                raise Exception(f"Error in creating Destination File: {v}")
