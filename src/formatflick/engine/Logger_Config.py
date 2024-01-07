import logging
import sys

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Create a StreamHandler and set the formatter
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

# Create a FileHandler and set the formatter
# file_handler = logging.FileHandler('project.log')
# file_handler.setFormatter(formatter)

# Create the logger
logger = logging.getLogger('project_logger')
logger.setLevel(logging.DEBUG)  # Set the global logging level

# Add the handlers to the logger
logger.addHandler(stream_handler)
# logger.addHandler(file_handler)
