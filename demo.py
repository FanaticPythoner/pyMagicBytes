from DBFileTypes import _getAllFileTypes
from GetFileType import FileObject
obj = FileObject(r"SampleFile\file_example_AVI_480_750kB.avi")
ListOfPossibleFileTypes = obj.getPossibleTypes()