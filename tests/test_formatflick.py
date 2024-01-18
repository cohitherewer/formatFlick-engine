import unittest
from src.formatflick.formatflick import Formatflick as ffe
# import pandas
import os
import re

PATH = os.path.join(os.getcwd(), "sample_files")


def get_custom_path(_path):
    return os.path.join(PATH, _path)


class TestFormatFlick(unittest.TestCase):
    def setUp(self):
        # source file paths
        self.source_json = get_custom_path("samplejson.json")
        self.source_csv = get_custom_path("samplecsv.csv")
        self.source_tsv = get_custom_path("sampletsv.tsv")

        # destination file paths
        self.destination_json = get_custom_path("resultjson.json")
        self.destination_csv = get_custom_path("resultcsv.csv")
        self.destination_tsv = get_custom_path("resulttsv.tsv")

        # self.current_format = None

    def tearDown(self):
        # os.remove(self.destination_csv)
        _files = os.listdir(PATH)
        files = [ff for ff in _files if ff.startswith("result")]
        for ff in files:
            # os.remove(get_custom_path(ff))
            pass
        print("File Deleted Successfully...")

    def test_json_to_csv(self):
        obj = ffe(self.source_json, self.destination_csv)
        obj.convert()
        self.assertTrue(os.path.exists(self.destination_csv))

    def test_json_to_tsv(self):
        obj = ffe(self.source_json, self.destination_tsv)
        obj.convert()
        self.assertTrue(os.path.exists(self.destination_tsv))

    def test_csv_to_json(self):
        obj = ffe(self.source_csv, self.destination_json)
        obj.convert()
        self.assertTrue(os.path.exists(self.destination_json))

    def test_tsv_to_json(self):
        obj = ffe(self.source_tsv, self.destination_json)
        obj.convert()
        self.assertTrue(os.path.exists(self.destination_json))


if __name__ == '__main__':
    unittest.main()
