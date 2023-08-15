#!/usr/bin/env python3
import os
print(os.getcwd()) # the same as pwd in terminal
print(os.listdir("exampleDir"))
dir= "exampleDir"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
# Output would be:

"""
/home/developer/OS-python/osModule
['images', 'example.html', 'example.ico']
exampleDir/images is a directory
exampleDir/example.html is a file
exampleDir/example.ico is a file
"""