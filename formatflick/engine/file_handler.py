class handler:
    """placeholder function for handling files"""
    def __init__(self, file_path):
        """generic class format for file format"""
        self.file_path = file_path
        self.content = self.file_content()

    def is_password_protected(self):
        """util function to check if the file is password protected or not"""

    def have_read_access(self):
        """util function to check if the file has read access or not"""

    def is_valid_format(self):
        """
        placeholder function to check for valid format of a particular file
        User can change it as it is
        """

    def file_content(self):
        """open the file to see the file content"""
        with open(self.file_path) as file:
            _content = file.read()
        return _content
