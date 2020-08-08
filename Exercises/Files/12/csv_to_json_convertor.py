# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:


import csv;
import json

csv_file = open('csv_file.txt','r')
fieldNames = ['club','city','country']
file_contents = [file for file in csv.DictReader(csv_file,fieldNames)]
csv_file.close()
json_file = open('json_file.txt','w')
json.dump(file_contents,json_file)
json_file.close()