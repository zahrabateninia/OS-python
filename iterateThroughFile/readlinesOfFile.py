#!/usr/bin/env python3

file = open("hafezQuote.txt")
lines = file.readlines() 
file.close()
lines.sort()
print(lines)