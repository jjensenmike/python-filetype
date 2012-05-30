import filetype as ft
from os import path
import unittest

file_list = [
    ("test.bz2", "bz2"),
    ("test.csv", "csv"),
    ("test.gz", "gz"),
    ("test.rar", "rar"),
    ("test.tar", "tar"),
    ("test.tar.gz", "gz"),
    ("test.txt", "txt"),
    ("test.xml", "xml"),
    ("test.zip", "zip")
    ]

type_list = [
    ("gz", True, False),
    ("bz2", True, False),
    ("zip", False, True),
    ("rar", False, True),
    ("tar", False, True),
    ("txt", False, False)
    ]

file_type_list = [
    ("test.gz", True, False),
    ("test.tar", False, True),
    ("test.xml", False, False)
    ]

class TestFileType(unittest.TestCase):

    def testFileTypes(self):
        for filename, type_response in file_list:
            filename = path.join(path.dirname(__file__), "testdata", filename)
            self.assertEqual(type_response, ft.get_type(filename))

    def testTypes(self):
        for f_type, compressed, archived in type_list:
            self.assertEqual(compressed, ft.is_compression_by_type(f_type))
            self.assertEqual(archived, ft.is_archived_by_type(f_type))

    def testFileCompressionArchived(self):
        for filename, compressed, archived in file_type_list:
            filename = path.join(path.dirname(__file__), "testdata", filename)
            self.assertEqual(compressed, ft.is_compression(filename))
            self.assertEqual(archived, ft.is_archived(filename))

if __name__ == '__main__':
	unittest.main()
