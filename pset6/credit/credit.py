# Import library
from cs50 import get_int

# Get credit card number
credit = get_int("card number: ")

# Check cash greater than 0
while True:
    if credit > 0:
        break
    else:
        # Else prompt again
        credit = get_int("Card number: ")

# Get first digit
first_dig = int(str(credit)[:1])

# Get first two digit
first2_dig = int(str(credit)[:2])

# Number to String
cred_str = str(credit)

# Temp varibales
temp = ""
tot_temp = 0
tot = 0

# Is it divisible by 2?
if len(cred_str) % 2 == 0:
    for j in reversed(range(0, len(cred_str), 2)):
        if j < len(cred_str)-1 and j % 2 == 0:
            num = int(cred_str[j]) * 2
            temp = temp + str(num)
else:
    for j in reversed(range(0, len(cred_str))):
        if j < len(cred_str)-1 and j % 2 != 0:
            num = int(cred_str[j]) * 2
            temp = temp + str(num)

# Sum total temp
for n in range(len(temp)):
    tot_temp = tot_temp + int(temp[n])

# Get Total
if len(cred_str) % 2 == 0:
    for m in range(0, len(cred_str)):
        if m > 0 and m % 2 != 0:
            num2 = int(cred_str[m])
            tot = tot + num2
else:
    for m in range(0, len(cred_str), 2):
        if m == 0 or m > 1:
            num2 = int(cred_str[m])
            tot = tot + num2

# Validate the Credit Card by summing both parts
vald = tot_temp + tot
if vald % 10 == 0:
    # AMEX
    if first2_dig == 34 or first2_dig == 37:
        # Check Length
        if len(str(credit)) == 15:
            print("AMEX")
        else:
            print("INVALID")
    # Mastercard
    elif first2_dig == 51 or first2_dig == 52 or first2_dig == 53 or first2_dig == 54 or first2_dig == 55:
        # Check Length
        if len(str(credit)) == 16:
            print("MASTERCARD")
        else:
            print("INVALID")
    # VISA
    elif first_dig == 4:
        # Check Length
        if len(str(credit)) == 13 or len(str(credit)) == 16:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
# Else print invalid
else:
    print("INVALID")