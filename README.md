# pyMagicBytes (0 EXTERNAL DEPENDENCY) 
This tool is basically a Database of 750+ Magic Bytes (Files Signatures) with a 2 lines python wraper to find the type of any file you trow at it.

I wrote this tool for Hacking Competition purpose. However, you can use it for whatever you want. Feel free to tell me if any Magic Bytes in the "database" is wrong.

### Language: ### 

- Tested in Python 3.6, should work in all Python 3 version.

### Limitations: ###

- Because a lot of files have the same Magic Bytes it is impossible (in most cases) to be 100% sure that the file your throwed at pyMagicBytes can be only one file type : This is why, when you call the *GetPossibleTypes()* function of a [*FileObject*](https://github.com/FanaticPythoner/pyMagicBytes#fileobject-class) it will return an array containing all possible files types (with some additionnal informations). See below for more details.


### Table of Contents: ###

- Classes
  - [*FileObject*](https://github.com/FanaticPythoner/pyMagicBytes#fileobject-class)
  
# Installation

- Download the repository

- Use the sample code below [*Usage / Code Sample*](https://github.com/FanaticPythoner/pyMagicBytes#usage--code-sample-) in the [*FileObject*](https://github.com/FanaticPythoner/pyMagicBytes#fileobject-class) class below as an example. Enjoy.


# FileObject Class

### Description : ###
Open a file stream of a given file you provided the Path in the constructor. It still works if you provide a relative path.

### Usage / Code sample : ###
*This example create a FileObject object then find the file type of the file which the path was specified in the constructor. The file types are sorted by the most probable file type to the less probable.*
```python
from DBFileTypes import _getAllFileTypes
obj = FileObject(r"SampleFile\file_example_AVI_480_750kB.avi")
ListOfPossibleFileTypes = obj.getPossibleTypes()
```
This is the value of the variable *ListOfPossibleFileTypes* of the previous example when debugging with Visual Studio Code:

![alt text](https://i.imgur.com/Y1qB1RK.jpg)
