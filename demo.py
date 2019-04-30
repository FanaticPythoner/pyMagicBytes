# Autor : FanaticPythoner.
# Please read the "LICENSE" file before doing anything.

from pyMagicBytes import FileObject

#The 'updateDB' argument will specify to pyMagicBytes if it needs to update the DB to the newest version from GitHub. Optional argument.
obj = FileObject(r"SampleFile\file_example_AVI_480_750kB.avi", updateDB=True)

#The 'ReturnArray' argument will specify if pyMagicBytes returns an array or a nice little printable string. In this case, a string.
ListOfPossibleFileTypes = obj.getPossibleTypes(ReturnArray=False)

print(ListOfPossibleFileTypes)
