import json
import os.path
import xml.etree.ElementTree as ET
from ..global_var import *
from html5validate import validate

# VALID_EXTENSIONS = [".csv", ".json", ".tsv", ".html"]


def get_file_name(source):
    """Utility function to get the file name"""
    try:
        return True, os.path.basename(source)
    except Exception as err:
        return False, err


def get_extension(source):
    """Utility function to get the file_extension"""
    try:
        return True, os.path.splitext(source)[1]
    except Exception as err:
        return False, err


def validate_extension(extension):
    """Utility function to validate an extension"""
    return extension in VALID_EXTENSIONS


def validate_json(file_path):
    """utility function to validate a json file"""
    try:
        with open(file_path, 'r') as file:
            json_object = json.load(file)
            return True, json_object
    except (json.JSONDecodeError, FileNotFoundError) as err:
        return False, err


def validate_xml(source):
    """utility function to validate an xml file"""
    try:
        return True, ET.parse(source)
    except Exception as err:
        return False, err


def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            pass
        return True, file_path
    except Exception as err:
        return False, err


# Utility functions for validating HTML5
def validate_html(file_path):
    """
    Utility function to validate a html file
    """
    with open(file_path, "r") as file:
        content = file.readlines()
        if isinstance(content, list):
            content = content[0]
        validate(content)
        return True
