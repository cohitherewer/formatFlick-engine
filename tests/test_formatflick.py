# import unittest
# from formatflick.formatflick import Formatflick
# # import pandas
# import os
#
#
# class TestFormatFlick(unittest.TestCase):
#     def setUp(self):
#         self.source_json = os.path.join(os.getcwd(),"tests","sample_files", "samplejson.json")
#         # self.destionation_csv = os.path.join(os.getcwd(),"tests","sample_files","sample")
#     def test_json_no_dest_ext(self):
#         with self.assertRaises(Exception) as context:
#             obj = Formatflick(self.source_json)
#             obj.convert()
#         self.assertEqual(str(context.exception), "Either destination or destination_extension should be given.")
#
#     def test_json_no_dest(self):
#         destination = os.path.join(os.getcwd(),"tests","sample_files")
#         with self.assertRaises(Exception) as context:
#             obj = Formatflick(self.source_json, destination)
#             obj.convert()
#         print(str(context.exception))
#         self.assertEqual(True, False)
# if __name__ == '__main__':
#     unittest.main()
