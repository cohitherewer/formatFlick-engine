from input_handler import input_handler

class formatflick:
    def __init__(self,*args, **kwargs):
        self.file_path = kwargs.get("file_path", None)
        # self.file_path2 = kwargs.get("file_path2", None)
        self.converted_extension = kwargs.get("dest",None)

        if self.file_path1 is None:
            raise Exception("Expected a file path. Instead got one or less")
        
        if self.converted_extension is None:
            raise Exception("Exception ocuured: no destination file extension")
        
        # validate the file path
        input_handler.validate_file_path(self.file_path1)
        # validate the extention
        input_handler.validate_extention()
        # validate the file extentions
        input_handler.extract_file_extension(self.file_path1)
        
        # create or update the destination file
        self.dest_file = kwargs.get("dest_file", None)
        if self.dest_file is None:
            print("No Destination file given")
            print(f"Creating a destination file named dest.{self.converted_extension}...")
            self.dest_file = "dest"
        input_handler.create_new_file(self.dest_file, self.converted_extension)


    def convert(self):
        pass

    