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

# Check for input (house)
if len(sys.argv) == 2:
    house = sys.argv[1]
else:
    sys.exit('Error - Interst CSV File')

# Query db
sql = "SELECT first,middle,last,birth FROM students WHERE house = '%s' order by last, first" %house

# Save result
result = db.execute(sql)

# Print each row
for x in range(len(result)):
    if result[x]['middle'] == None:
        print("%s %s, born %i" %(result[x]['first'], result[x]['last'], result[x]['birth']))
    else:
        print("%s %s %s, born %i" %(result[x]['first'], result[x]['middle'], result[x]['last'], result[x]['birth']))