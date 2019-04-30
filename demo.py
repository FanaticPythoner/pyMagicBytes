# Autor : FanaticPythoner.
# Please read the "LICENSE" file before doing anything.

from GetFileType import FileObject
obj = FileObject(r"SampleFile\file_example_AVI_480_750kB.avi")
ListOfPossibleFileTypes = obj.getPossibleTypes()
