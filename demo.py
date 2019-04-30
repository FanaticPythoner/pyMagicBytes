# Autor : FanaticPythoner.
# Please read the "LICENSE" file before doing anything.

from GetFileType import FileObject

#This will update the DB to the newest version from GitHub. Optional argument.
obj = FileObject(r"SampleFile\file_example_AVI_480_750kB.avi", updateDB=True)
ListOfPossibleFileTypes = obj.getPossibleTypes()
