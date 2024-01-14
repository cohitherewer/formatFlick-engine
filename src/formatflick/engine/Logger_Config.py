import logging
import sys

log_level_map = {
    0: logging.DEBUG,
    1: logging.INFO,
    2: logging.WARNING,
    3: logging.ERROR,
    4: logging.CRITICAL
}


class create_logger:
    def __init__(self, verb):
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        self.logger = logging.getLogger('project_logger')

        if log_level_map.get(verb, None) is None:
            raise Exception(f"{verb} is not a valid verbosity level")
        self.level = log_level_map.get(verb, None)
        if self.level is None:
            raise Exception(f"Please send verb")

        self.logger.setLevel(self.level)
        self.logger.addHandler(stream_handler)

    # Utility function for getting log messages
    # logs unsupported file conversion
    def log_unsupported_file_conversion_error(self, source, destination):
        self.logger.error(f"{source} to {destination} is unsupported file conversion by default")

    # log processing time
    def log_time(self, start_time, end_time):
        self.logger.info(f"Time Taken: {end_time - start_time}")

    # log validation of files
    def log_validating_file_encoding(self, source):
        # file encoding validation stats
        self.logger.info(f"Validating {source} Encoding")

    def log_validated_file_encoding(self, source):
        # valid file encoding
        self.logger.info(f"{source} encoding is validated")

    def log_invalid_file_encoding(self, source):
        # invalid file encoding
        self.logger.error(f"Invalid file encoding for {source}")

    # log file name handling
    def log_filename_extraction_error(self, source):
        # log file name extraction error
        self.logger.error(f"Error occurred while extracting File Name: {source}", exc_info=False)

    # log file extension handling
    def log_extension_extraction_msg(self, src):
        self.logger.info(f"Validating the {src} file extension")

    def log_extension_extraction_error(self, extension):
        # log file extension error
        self.logger.error(f"Error occurred while getting File Extension: {extension}", exc_info=False)

    def log_valid_extension_msg(self):
        # log valid file extension
        self.logger.info("Valid file extension")

    def log_invalid_extension_error(self, extension):
        self.logger.error(f"{extension} is not a valid File Extension")

    def log_invalid_file_path(self, path):
        self.logger.error(f"{path} does not exist")

    def log_path_exists_waring(self, path):
        # path related warning
        self.logger.warning(f"Path: {path} already exists")

    def log_create_file(self):
        # file creation => successfully
        self.logger.info("Destination File created successfully")

    def log_create_file_error(self):
        self.logger.error("Error in creating Destination File")

    # custom log
    def log_custom_message(self, *args, **kwargs):
        """
        Custom log message. This function can be changed for users own need.
        """
        msg = kwargs.get("msg", None)
        self.logger.info(msg)
