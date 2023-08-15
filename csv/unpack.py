#!/usr/bin/env python3 
import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, age, role = row
    print("Name: {}, Age: {}, Role:{}".format(name, age, role))
f.close()