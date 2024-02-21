"""
This file contains all the necessary functions to modify a json object
- read_html file
"""


def read_html(file_path):
    """reading html file"""
    with open(file_path, "r") as file:
        obj = file.read()
    return obj

def html_engine_handle(source, log, *args, **kwargs):
    """
    Handles the html object as it it.
    Important point to note that the html should contain table tag and it should be validated at first
    """
