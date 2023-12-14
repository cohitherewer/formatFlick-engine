from file_handler import handler
import json

def flatten_json_util(json_data, parent_key='',sep='_'):
    """flatten the json file"""
    flattened_dict = {}
    for key, value in json_data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_json_util(value, new_key, sep=sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict

class jason_handler(handler):
    """handles json file format"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def is_valid_format(self):
        print(self.content)
        try:
            json.loads(self.content)
            return True
        except json.JSONDecodeError as err:
            raise Exception(f"Error occured during reading json file {err}")
    
    def flatten_json(self):
        flattened_json = flatten_json_util(self.content,'','_')
# if __name__=="__main__":
#     obj = jason_handler("thanks.json")
#     obj.is_valid_format()
