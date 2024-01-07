import json
import unittest
from formatflick.engine.handler import util
import os


def create_path(source):
    return os.path.join(os.getcwd(),"formatflick", "tests", "sample_files", source)


class TestUtil(unittest.TestCase):
    def setUp(self):
        self.json = create_path("samplejson.json")
        self.invalid_json = create_path("invalid_samplejson.json")

        self.xml = create_path("samplexml.xml")
        self.invalid_xml = create_path("invalid_samplexml.xml")

        self.file_path = create_path("samplefile.csv")
        self.invalid_file_path = os.path.join(os.getcwd(),"formatflick", "tests", "sample_files", "another", "samplefile.csv")

        self.valid_extension = util.VALID_EXTENSION

    def tearDown(self):
        try:
            os.remove(self.file_path)
            print("File Deleted Successfully")
        except Exception as err:
            pass

    def test_get_file_name(self):
        u, v = util.get_file_name(self.json)
        self.assertTrue(u)
        self.assertEqual(v, "samplejson.json")

    # def test_get_file_name_with_error(self):
    #     u, v = util.get_file_name("error/_file")
    #     self.assertEqual(u,False)

    def test_get_extension(self):
        u, v = util.get_extension("samplejson.json")
        self.assertTrue(u)
        self.assertEqual(v, ".json")

    def test_validate_extension(self):
        u = util.validate_extension(".csv")
        self.assertTrue(u)

    def test_validate_extension_with_error(self):
        v = util.validate_extension(".py")
        self.assertFalse(v)

    def test_validate_json(self):
        u, v = util.validate_json(self.json)
        self.assertTrue(u)

    def test_validate_json_with_error(self):
        u, v = util.validate_json(self.invalid_json)
        self.assertFalse(u)

    def test_validate_xml(self):
        u, v = util.validate_xml(self.xml)
        self.assertTrue(u)

    def test_validate_xml_with_error(self):
        u, v = util.validate_xml(self.invalid_xml)
        self.assertFalse(u)

    def test_create_file(self):
        u, v = util.create_file(self.file_path)
        self.assertTrue(u)
        self.assertEqual(v, self.file_path)

    def test_create_file_error(self):
        u, v = util.create_file(self.invalid_file_path)
        self.assertFalse(u)


if __name__ == '__main__':
    unittest.main()
