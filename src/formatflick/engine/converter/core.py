from src.formatflick.engine import handler
from .text_engine import json_engine as jengine
from .text_engine import csv_engine as cengine
from ..global_var import *


class Core_engine:
    """Core_engine that handles the conversion"""

    def __init__(self, source, log, *args, **kwargs):
        """Initialization for Core_engine"""
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

    # def json_to_util(self, *args, **kwargs):
    #     """
    #     handle json to csv and tsv file conversion.
    #     csv and tsv files can be handled in the same way just the delimiter is different
    #     """
    #     extension = kwargs.get("extension", None)
    #     assert extension is not None
    #     self.log.info(f"Converting from .json to {extension}")
    #     json_obj = utils.read_json(self.source)
    #     flatten_json_obj = []
    #     for item in json_obj:
    #         flatten_json_obj.append(utils.flatten_json(item))
    #     headers = list(set(key for entry in flatten_json_obj for key in entry.keys()))
    #     sep = ',' if extension == ".csv" else '\t'
    #     with open(self.destination, "w", newline='', encoding='utf-8') as file:
    #         writer = csv.DictWriter(file, fieldnames=headers, delimiter=sep)
    #         writer.writeheader()
    #         writer.writerows(flatten_json_obj)
    #     self.log.info("Conversion Complete")
    #     self.log.info(f"Resulting file can be seen at {self.destination}")

    def json_to_csv(self):
        """handles json to csv file conversion"""
        # self.json_to_util(extension=".csv")
        flatten_obj, headers = jengine.json_engine_handle(self.source, self.log)
        # t_dst = None
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

    # def to_json_util(self, extension):
    #     """handles csv/tsv to json file conversion"""
    #     self.log.info(f"Converting from {extension} to .json")
    #     self.log.info(f"Reading the {self.source} file...")
    #     sep = ',' if extension == ".csv" else '\t'
    #     data = utils.read_csv(self.source, delimiter=sep)
    #     self.log.info("Started Conversion...")
    #     with open(self.destination, 'w+') as json_file:
    #         json.dump(data, json_file, indent=2)
    #
    #     self.log.info("Conversion Complete")
    #     self.log.info(f"Resulting file can be seen at {self.destination}")

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
        # self.to_json_util(extension=".csv")

    def csv_to_tsv(self):
        """handles csv to tsv file conversion"""

        df = cengine.csv_engine_handle(self.source, extension=".csv", log=self.log)
        # df.to_csv(self.destination, sep='\t', index=False)

        obj = cengine.csv_engine_convert(destination=self.t_dst,
                                         log=self.log,
                                         obj=df,
                                         extension=".tsv",
                                         sep='\t',
                                         index=False,
                                         mode=self.mode
                                         )
        return obj

    def tsv_to_csv(self):
        """handles tsv to csv file conversion"""
        # self.log.info("Converting from .tsv to .csv")
        # self.log.info(f"Reading the {self.source} file...")
        # df = utils.read_csv(self.source, delimiter='\t')
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
        # df.to_csv(self.destination, index=False)
        # self.log.info("Conversion Complete")
        # self.log.info(f"Resulting file can be seen at {self.destination}")

    def json_to_tsv(self):
        """handles json to tsv file conversion"""
        # self.json_to_util(extension=".tsv")
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

    def tsv_to_json(self):
        """handles tsv to json file conversion"""
        df = cengine.csv_engine_handle(self.source, extension=".tsv", log=self.log)
        obj = jengine.json_engine_convert(self.t_dst, self.log, data=df, index=2, mode=self.mode)
        return obj
        # self.to_json_util(extension=".tsv")

    def custom_convert(self):
        """this function can be overwritten for custom implementations"""
        pass

    def __del__(self):
        if self.mode == FILE_MODE:
            self.log.log_process_completion(destination=self.destination)
        else:
            self.log.log_process_completion(destination=self.extension)
