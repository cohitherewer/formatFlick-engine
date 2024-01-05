from file_handler import handler
import pandas as pd

"""
Right Now the implementation is based on Pandas. So there is some limitations based on the file size we can use
"""

class csv_handler(handler):
    """handles csv file format"""
    def __init__(self, file_path):
        super().__init__(file_path)

    def is_valid_format(self):
        print(self.content)
        try:
            self.content=pd.read_csv(self.content)
            return True
        except Exception as err:
            raise Exception(f"Error occured during reading csv file {err}")
    
    