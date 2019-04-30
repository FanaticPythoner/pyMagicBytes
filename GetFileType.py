# Autor : FanaticPythoner.
# Please read the "LICENSE" file before doing anything.

from DBFileTypes import _getAllFileTypes
import os

class FileObject:
    def __init__(self, filePath):
        self.allFileTypes = _getAllFileTypes()
        self.fileStream = open(os.path.abspath(filePath),'rb')

    def getPossibleTypes(self):
        typesFound = []
        for row in self.allFileTypes:
            matchedCurrentFileType = True
            size, offs, sign, ext, desc = row.split('|')
            size = int(size)
            offsArr = offs.split('..')
            for off in offsArr:
                self.fileStream.seek(int(off))
                redBytesString = self.fileStream.read(size).hex().upper()
                for byteHex, hexByteSign in zip(redBytesString, sign):
                    if hexByteSign != '?':
                        if hexByteSign != byteHex:
                            matchedCurrentFileType = False
                            break
            if matchedCurrentFileType:
                typesFound.append([('Bytes Offsets', offs.replace('..',' and ')), ('File Signature', sign), ('File Extension', ext), ('Description', desc)])
        return typesFound
