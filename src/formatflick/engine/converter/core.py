from .text_engine import json_engine as jengine
from .text_engine import csv_engine as cengine
from .text_engine import xlsx_engine as xengine
from formatflick.global_var import *


class Core_engine:
    """
    This class handles all the necessary conversion such as json to csv etc.
    To handle all the conversions it defines all types of class for every such conversions
    """

    def __init__(self, source, log, *args, **kwargs):
        """
        Initialisation of Core_engine class.
        Input:
        - source:
            validated source file path
            point to note that at this point the source file is validated before
        - log:
            object of logger class.
            Handles all type of logging
        - *args (Optional)
        - **kwargs:
            1. destination (Optional):
                validated destination.
                Same as a source file path, at this point the destination file path is validated
                If this parameter not passed module determines the further proceeding with respect to the value of mode
            2. mode(optional)
                by default, it is set as 'file' mode
            3. extension:
                In file mode, an extension should be given other it will throw error.

        """
        self.log = log
        self.log.log_custom_message(msg="Initiating Process...")

        self.source = source  # get the source
        # self.destination = destination
        self.mode = kwargs.get("mode", FILE_MODE)  # get the mode
        if self.mode == FILE_MODE:
            # for file mode
            self.destination = kwargs.get("destination", None)
            if self.destination is None:
                raise Exception("For 'file' mode give the proper destination")
            self.log.log_process_initialization(source=self.source,
                                                destination=self.destination)
            self.t_dst = self.destination
        else:
            self.extension = kwargs.get("extension", None)
            if self.extension is None:
                raise Exception("For non 'file' mode give the proper extension")
            self.log.log_process_initialization(source=self.source,
                                                destination=self.extension)
            self.t_dst = self.extension

    # #################################
    # SOURCE FILE: JSON
    # #################################
    def json_to_tsv(self):
        """handles json to tsv file conversion"""
        flatten_obj, headers = jengine.json_engine_handle(self.source, self.log)
        obj = cengine.csv_engine_convert(destination=self.t_dst,
                                         obj=flatten_obj,
                                         sep='\t',
                                         extension=".json",
                                         log=self.log,
                                         headers=headers,
                                         newline='',
                                         encoding='utf-8',
                                         mode=self.mode
                                         )
        return obj

    def json_to_csv(self):
        """handles json to csv file conversion"""
        flatten_obj, headers = jengine.json_engine_handle(self.source, self.log)
        obj = cengine.csv_engine_convert(destination=self.t_dst,
                                         obj=flatten_obj,
                                         sep=',',
                                         extension=".json",
                                         log=self.log,
                                         headers=headers,
                                         newline='',
                                         encoding='utf-8',
                                         mode=self.mode
                                         )
        return obj

    def json_to_html(self):
        pass

    def json_to_xlsx(self):
        pass

    # #################################
    # SOURCE FILE: CSV
    # #################################

    def csv_to_json(self):
        """handles csv to json file conversion"""
        df = cengine.csv_engine_handle(self.source, extension=".csv", log=self.log)
        obj = jengine.json_engine_convert(destination=self.t_dst,
                                          log=self.log,
                                          data=df,
                                          indent=2,
                                          mode=self.mode
                                          )
        return obj

    def csv_to_tsv(self):
        """handles csv to tsv file conversion"""
        df = cengine.csv_engine_handle(self.source, extension=".csv", log=self.log)

        obj = cengine.csv_engine_convert(destination=self.t_dst,
                                         log=self.log,
                                         obj=df,
                                         extension=".tsv",
                                         sep='\t',
                                         index=False,
                                         mode=self.mode
                                         )
        return obj

    def csv_to_xlsx(self):
        pass

    def csv_to_html(self):
        pass

    # #################################
    # SOURCE FILE: TSV
    # #################################
    def tsv_to_csv(self):
        """handles tsv to csv file conversion"""
        df = cengine.csv_engine_handle(self.source, extension=".tsv", log=self.log)
        obj = cengine.csv_engine_convert(destination=self.t_dst,
                                         log=self.log,
                                         obj=df,
                                         extension=".csv",
                                         sep=' ',
                                         index=False,
                                         mode=self.mode
                                         )
        return obj

    def tsv_to_json(self):
        """handles tsv to json file conversion"""
        df = cengine.csv_engine_handle(self.source, extension=".tsv", log=self.log)
        obj = jengine.json_engine_convert(self.t_dst, self.log, data=df, index=2, mode=self.mode)
        return obj

    def tsv_to_html(self):
        pass

    def tsv_to_xlsx(self):
        pass

    # #################################
    # SOURCE FILE: HTML
    # #################################
    def html_to_json(self):
        pass

    def html_to_csv(self):
        pass

    def html_to_tsv(self):
        pass

    def html_to_xlsx(self):
        pass

    # #################################
    # SOURCE FILE: XLSX
    # #################################
    def xlsx_to_csv(self):
        df = xengine.xlsx_engine_handle(source=self.source, log=self.log)
        return None

    def xlsx_to_tsv(self):
        pass

    def xlsx_to_json(self):
        df = xengine.xlsx_engine_handle(source=self.source,log=self.log, extension=".json")
        return None

    def xlsx_to_html(self):
        pass

    def custom_convert(self):
        """this function can be overwritten for custom implementations"""
        pass

    def __del__(self):
        """
        Called when the process in done with its execution. Right now Simple logger is being used.
        The functionality can be extended. 
        """
        if self.mode == FILE_MODE:
            self.log.log_process_completion(destination=self.destination)
        else:
            self.log.log_process_completion(destination=self.extension)
