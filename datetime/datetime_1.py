#!/usr/bin/env python3
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  readableTime = str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 
  return (readableTime[:10])

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd