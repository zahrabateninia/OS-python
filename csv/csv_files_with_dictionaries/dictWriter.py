#!/usr/bin/env python3
import csv
users = [{"name": "Ryan", "username": "imryan", "department": "IT infrastructure"},
{"name": "Jack", "username": "lionlin", "department": "User Experience Research"},
{"name": "Charlie", "username": "labalabla", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    