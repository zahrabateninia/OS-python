#!/usr/bin/env python3
# Access the environment variable:
import os
print("HOME: "+ os.environ.get("HOME", "")) # get method allows us to specify a default value when the key we're looking for isn't present in the dictio
print("SHELL: "+ os.environ.get("SHELL", ""))
print("FRUIT: "+ os.environ.get("FRUIT", ""))