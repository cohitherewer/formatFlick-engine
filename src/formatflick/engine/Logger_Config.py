import logging
import sys

log_level_map = {
    0: logging.DEBUG,
    1: logging.INFO,
    2: logging.WARNING,
    3: logging.ERROR,
    4: logging.CRITICAL
}


def create_logger(verb):
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger('project_logger')

    if log_level_map.get(verb, None) is None:
        raise Exception(f"{verb} is not a valid verbosity level")
    logger.setLevel(log_level_map.get(verb, None))
    logger.addHandler(stream_handler)

    return logger
