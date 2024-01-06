import os
import util
from formatflick.engine.Logger_Config import logger as log


class DestinationFile_handler:
    """
    Handles checks for destination files
    Possible Checks are
    - if the file exists in the path or not
        - if it does not exist raise exception
    - the file is csv, xml or json or not
    """

    def __init__(self, destination, dest_extension):
        if not (destination or dest_extension):
            raise Exception("Either destination or dest_extension should be given.")

        self.destination = destination or os.path.join(os.getcwd(), 'result' + '.' + dest_extension)
        self.destination_file = destination or 'result'
        self.extension = dest_extension or self.get_extension()
        self.validate_extension()

    def create_dest_file(self):
        pass

    def validate_extension(self):
        log.info("Validating File Extension of Destination File")
        if util.validate_extension(self.extension):
            log.info("Valid File Extension")
        else:
            log.error(f"{self.extension} is not a valid File Extension")
            raise Exception(f"{self.extension} is not a valid File Extension")

    def get_extension(self):
        log.info("Getting the Extension")
        u, v = util.get_extension(self.destination_file)
        if u:
            self.extension = v
        else:
            log.error(f"Error occurred while getting File Extension: {v}")
            raise Exception(f"Error while extracting file extension from {self.destination_file}: {v}")
