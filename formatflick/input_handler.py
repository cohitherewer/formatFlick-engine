"""
This file handles the incoming input.
Takes two files and checks its the valid extention or not
"""
import os

class input_handler:
    def __init__(self,*args, **kwargs) -> None:
        # self.file_path1 = file_path1
        # self.file_path2 = file_path2
        self.valid_extentions = [".csv",".xml",".xlsx",".json"]
    
    @staticmethod
    def validate_file_path(file_path):
        """helper function to validate the file path"""
        if not os.path.exists(file_path):
            raise Exception(f"File Path {file_path} does not exists")
    
    def extract_file_extension(self,file_path):
        """Helper function to extract the file extention"""
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() not in self.valid_extentions:
            raise Exception(f"File Path {file_path} has no valid extension")
        return file_extension.lower()
    
    def validate_extention(self,extension):
        try:
            assert type(extension) == str
        except TypeError as err:
            raise Exception(f"Exception occured {err}")
        
        extension = "."+extension.lower()
        if extension not in self.valid_extentions:
            raise Exception("Destination file extention is not valid")    
        return True
    
    @staticmethod
    def create_new_file(dest_file,extension):
        try:
            file_path = os.path.join(os.getcwd(),dest_file+extension)
            with open(file_path,"w") as dest:
                print("File Created Succesfully")
        except Exception as err:
            raise Exception(f"Exception ocuured: {err}")
    
