from flick import *
from engine.xEngine import xEngine, dest_xEngine
from engine.jEngine import jEngine, dest_jEngine
from engine.cEngine import cEngine, dest_cEngine


class formatflick(flick):
    def __init__(self, source: Path, destination: Path = None, destination_extension: str = None, verbosity: int = None,
                 mode: str = FILE_MODE, *args, **kwargs):
        """
        Initialises as instance of formatflick class with the provided source and some optional parameters:
        Right now this module operates two modes => 'file' and 'nfile'
        - 'file' mode will produce a destination file (which will may or may nor be provided by user)
        - 'nfile' mode will produce a destination object (which should be provided by the user)

        Inputs are as follows (an Extensive list)
        1. source: source file path. Ensure that you have entered path in accordance to the os
        2. destination:
            By default, it is set as None
        3. destination_extension:
            By default, it is set as None
            Remember to you have to put the number in such a way that module should be able to extract the extention to which you want to conver
            You either have to provide destination or destination extention.
            Below are some combinations of destination and destination_extension that will work,
                - destination = None and destination_extension = <dot> <any valid extension>
                - destination = <file path with a valid extension> and destination_extension (will be ignored)
        4. mode:
            There are two file modes for formatflick module(optional field)
            The value of mode is set to 'file' mode
                - 'file' outputs the resultant data into destination file
                - 'nfile' outputs the resultant data into destination file and also returns a dataframe
        5. verbosity:
            verbosity defines the level of logging user want while executing the module.
            The values are consistent with the python logging module;
            By default, it is set to 3
        """
        super().__init__(source, destination, destination_extension, verbosity, mode, *args, **kwargs)

        # for formatflick the default behavior is FILE_MODE

        if self.mode is None:
            self.mode = FILE_MODE

        # Check the source file is valid or not
        self.check_source_validity()

        # check the destination file, extensions are valid or not
        self.check_destination_validity()

        # check the validity of conversion
        self.is_valid_conversion()

    def check_source_validity(self) -> None:
        """
        Utility function to check if the source is valid or not
        In this function the followings are checked
        - source file path exists or not
        - If exists check is the source extension is valid extension or not

        """
        # Check if the Source is valid or not
        #
        if not os.path.exists(self.source):
            raise Exception("The source path dont exits")
        self.source_extension = super().get_file_extension(self.source)
        if not self.is_valid_file_extension(self.source_extension):
            raise Exception(
                f"{self.source} do not have the valid extension"
            )

    def check_destination_validity(self) -> None:
        """
        Utility function to check if the destination file is valid or not
        Depending on the file_mode we decide what to do
        If file_mode:
            In this function, the following logic is implemented,
            - If destination and destination path both are none, raise an exception
            - If destination is None
                - check for destination_extension. If it is not a valid extension, raise an exception
                - if it is a valid exception, destination file name would be "result" and form the destination file path

        If nfile_mode:
            If the destination_extension is None we will raise Exception.
            Destination Path will be ignored
        """
        if self.is_file_mode():
            # Check if the destination and destination_extension both are none or not
            if self.destination is None and self.destination_extension is None:
                raise Exception("destination and destination_extension both cannot be None.")
            # At this point, one of them is not none
            # to Consider self.destination is None
            if self.destination is None:
                # Check self.destination_extension is a valid destination of not
                is_valid = super().is_valid_file_extension(self.destination_extension)
                if is_valid:
                    # form the destination file path, with "results" name
                    self.destination = os.path.join(os.getcwd(), "result", self.destination_extension)
            else:
                # At this point, the self.destination is not none
                self.destination_extension = super().get_file_extension(self.destination)
                # The destination extension returned contains "." as prefix
                if not self.is_valid_file_extension(self.destination_extension):
                    raise Exception(
                        f"{self.destination_extension} is not valid. The valid extensions are {VALID_EXTENSIONS}"
                    )
        else:
            if self.destination_extension is None:
                raise Exception("destination_extension cannot be None for nfile mode")
            else:
                _ = super().is_valid_file_extension(self.destination_extension)

    def is_valid_conversion(self):
        conversion_key = (self.source_extension, self.destination_extension)
        function_call_map = [
            #  source file is json
            (".json", ".csv"),
            (".json", ".tsv"),
            (".json", ".xml"),
            (".json", ".xlsx"),
            # source file is .csv
            (".csv", ".json"),
            (".csv", ".tsv"),
            (".csv", ".xml"),
            (".csv", ".xlsx"),
            # source file is .tsv
            (".tsv", ".csv"),
            (".tsv", ".json"),
            (".tsv", ".xml"),
            (".tsv", ".xlsx"),
            # source file is .xml
            (".html", ".csv"),
            (".html", ".json"),
            (".html", ".tsv"),
            (".html", ".xlsx"),
            # source file is xlsx
            (".xlsx", ".csv"),
            (".xlsx", ".json"),
            (".xlsx", ".tsv"),
            (".xlsx", ".xml")
        ]
        if conversion_key not in function_call_map:
            raise Exception(f"The following conversion between {self.source_extension} and {self.destination_extension} is not allowed")
        return conversion_key

    def convert(self):
        """
        convert method for formatflick. This method can only be called once the __init__method is called
        successfully. The __init__method will check all valid file formats, encoding etc. Convert method will call the
        engine and convert from source file to destination file, optionally returning the destination object as well.

        There is an important check the convert does. During initialization, the source and destination file
        validation is done Right now all file formats the formal flick support can be converted between each other,
        But there might possibility where all formats cannot be connected to other formats. To prevent that,
        we add an extra checks where all valid conversions will be mentioned In that it will be helpful to prevent an
        unwanted result and users can don't need to debug that yourselves.
        """
        _engine_ = None
        # initialize the source object
        if self.source_extension in [CSV,TSV,XLSX]:
            _engine_ = cEngine(self.source,mode=self.mode,source_extension=self.source_extension)
            # df = obj.read_file()
        elif self.source_extension == JSON:
            _engine_ = jEngine(self.source, mode=self.mode)
        elif self.source_extension == XML:
            _engine_ = xEngine(self.source,mode=self.mode)

        # read the source file
        obj = _engine_.read_file()
        d_obj = None
        if self.destination_extension in [CSV, TSV, XLSX]:
            d_obj = obj.to_csv()
        elif self.destination_extension == JSON:
            d_obj = obj.to_json()
        elif self.destination_extension == XML:
            d_obj = obj.to_xml()

        # convert to destination object
        if self.mode == FILE_MODE:
            d_engine = None
            if self.destination_extension in [CSV,TSV, XLSX]:
                d_engine = dest_cEngine(d_obj,self.destination, destination_extension=self.destination_extension)
            elif self.destination_extension == JSON:
                d_engine = dest_jEngine(d_obj,self.destination)
            elif self.destination_extension == XML:
                d_engine = dest_xEngine(d_obj, self.destination)

            # convert to destination obj
            d_engine.to_destination()

        return d_obj
