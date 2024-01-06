import json
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