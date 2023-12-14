from file_handler import handler
import json

class jason_handler(handler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def is_valid_format(self):
        print(self.content)
        try:
            json.loads(self.content)
            return True
        except json.JSONDecodeError as err:
            raise Exception(f"Error occured during reading json file {err}")
        
# if __name__=="__main__":
#     obj = jason_handler("thanks.json")
#     obj.is_valid_format()
