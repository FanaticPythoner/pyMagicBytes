# Autor : FanaticPythoner.
# Please read the "LICENSE" file before doing anything.

from os.path import abspath
from requests import get

def _getAllFileTypes():
    return open('DB','r').readlines()

def _updateDBFromGithub():
    try:
        newDB = get('https://raw.githubusercontent.com/FanaticPythoner/pyMagicBytes/master/DB').text
        with open('DB','w') as f:
            f.write(newDB)
    except Exception as e:
        return str(e.args)
    print('Updated DB successfully.')
    return 'Success'

class FileObject:
    def __init__(self, filePath, updateDB=False):
        if updateDB:
            output = _updateDBFromGithub()
            if output != 'Success':
                raise Exception('An error occured when trying to update the DB from Github: ' + output)
        self.allFileTypes = _getAllFileTypes()
        self.fileStream = open(abspath(filePath),'rb')

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
