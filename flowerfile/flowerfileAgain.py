"""processing the data without turning it into a dictinary """
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file
    rows = file.readlines()
    # Process each row
    for row in rows:
      if "name,color,type"  in row:
        continue
      fields = row.strip().split(",")
      # Format the return string for data rows only, skip over the header record with the field names
      return_string += "a {} {} is {}\n".format(fields[1], fields[0], fields[2])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))