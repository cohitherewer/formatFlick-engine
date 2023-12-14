class handler:
    def __init__(self, file_path):
        """generic class format for file format"""
        self.file_path = file_path
        self.content = self.file_content()

    def is_password_protected(self):
        """util function to check if the file is password protected or not"""
        pass

    def have_read_access(self):
        """util function to check if the file has read access or not"""
        pass

    def is_valid_format(self):
        pass

    def file_content(self):
        with open(self.file_path) as file:
            _content = file.read()
        return _content
