# Import
from cs50 import get_string
from cs50 import SQL
import cs50
import re
import sys
import csv
import pandas as pd
import itertools

# Connect db
db = SQL("sqlite:///students.db")

# Check for file
if len(sys.argv) == 2:
    file_csv = sys.argv[1]
else:
    sys.exit('Error - Interst CSV File')

# Open file
data = pd.read_csv(file_csv)
columns = ['first', 'middle', 'last', 'house', 'birth']
names = data['name'].tolist()
name_split = []
first_name = []
mid_name = []
last_name = []
data_to_sql = []
house = data['house'].tolist()
birth = data['birth'].tolist()
dict_of_lists = {}

# Loop through names and split
for x in range(len(names)):
    name_split.append(names[x].split(' ', 3))

# Loop through names splits
for x in range(len(name_split)):
    if len(name_split[x]) != 3:
        name_split[x].insert(1, 'None')

# Loop through names splits and save first,mid and last
for x in range(len(name_split)):
    first_name.append(name_split[x][0])
    mid_name.append(name_split[x][1])
    last_name.append(name_split[x][2])

# Pass data to DataFrame
data_full = pd.DataFrame(list(zip(first_name, mid_name, last_name, house, birth)),
               columns = columns)

# Pass columns names to dic
data_full_colm = data_full.columns
for column_name in (data_full_colm):
    temp_list = data_full[column_name].tolist()
    dict_of_lists[column_name] = temp_list

# Keys from dcit t columns names in sql
columns_sql = tuple(dict_of_lists.keys())
for x in range(len(data_full)):
    new = []
    for column_name in (data_full_colm):
        new.append(dict_of_lists[column_name][x])
    data_to_sql.append(tuple(new))

# Insert data in db
for x in range(len(data_to_sql)):
    print(data_to_sql[x])
    if data_to_sql[x][1] == 'None':
        sql = "INSERT INTO students(first,middle,last,house,birth) VALUES ('{}',NULL,'{}','{}','{}')".format(data_to_sql[x][0], data_to_sql[x][2], data_to_sql[x][3], data_to_sql[x][4])
        db.execute(sql)
    else:
        sql = "INSERT INTO students(first,middle,last,house,birth) VALUES {}".format(data_to_sql[x])
        db.execute(sql)