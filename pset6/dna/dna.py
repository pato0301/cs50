# Import library
from cs50 import get_string
import re
import sys
import csv

# Get files
file_db = sys.argv[1]
file_sq = sys.argv[2]

# Open sequence
sq = open("{}".format(file_sq), "r")
sq_str = sq.read()

# Open Database
reader = csv.reader(open(file_db, 'r'))
db_dic = {}

# Read each line of db
for row in reader:
    key = row[0]
    if key in db_dic:
        # Implement your duplicate row handling here
        pass
    db_dic[key] = row[1:]

# Get columns Headers
headers = db_dic['name']
n = len(sq_str)
len_head = len(headers)
list_values = []

# Loop through each column
for y in range(len_head):
    texto = db_dic['name'][y]
    len_text = len(texto)
    cur, maximo, loop_inc = 0, 0, 1
    # Loop through each row
    for x in range(0, n, loop_inc):
        if sq_str[x: (x + len_text)] in texto:
            cur += 1
            # Look sequence
            if (x < n - 1 and sq_str[x: (x + len_text)] == sq_str[x + len_text: (x + (len_text * 2))]):
                loop_inc = len_text
            else:
                if (cur > maximo):
                    maximo = cur
                    cur = 0
                else:
                    cur = 0
                loop_inc = 1
    # Append in alist
    list_values.append(str(maximo))

# Print name if exist
name_exist = False
for name, dna in db_dic.items():
    if dna == list_values:
        print(name)
        name_exist = True

# Else print 'No Match'
if not name_exist:
    print("No match")