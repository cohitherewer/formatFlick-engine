import json
import os.path
import xml.etree.ElementTree as ET

VALID_EXTENSION = [".csv", ".csv", ".json"]


def get_file_name(source):
    """
    Util function to get the file name
    """
    try:
        return True, os.path.basename(source)
    except Exception as err:
        return False, err


def get_extension(source):
    """
    Util function to get the file_extension
    """
    try:
        return True, os.path.splitext(source)[1]
    except Exception as err:
        return False, err


def validate_extension(extension):
    """Util function to validate an extension"""
    return extension in VALID_EXTENSION


def validate_json(file_path):
    """
    validating a json file
    """
    try:
        with open(file_path, 'r') as file:
            json_object = json.load(file)
            return True, json_object
    except (json.JSONDecodeError, FileNotFoundError) as err:
        return False, err


def validate_xml(source):
    try:
        return True, ET.parse(source)
    except Exception as err:
        return False, err


def create_file(file_path):
    try:
        with open(file_path,'w') as file:
            pass
        return True, file_path
    except Exception as err:
        return False, err
