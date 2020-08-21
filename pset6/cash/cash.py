# Import library
from cs50 import get_int, get_float

# Get cash
cash = get_float("Change owed: ")

# Check cash greater than 0
while True:
    if cash > 0:
        break
    else:
        # Else prompt again
        cash = get_float("Change owed: ")

# Define coins
quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01

# Define number of each coins to return
n_qrt = 0
n_dim = 0
n_nik = 0
n_pen = 0

# Calculate number of coins
# Quarters
n_qrt = cash // quarters
mod_qrt = round(cash % quarters, 2)

# Dimes
n_dim = mod_qrt // dimes
mod_dim = round(round(cash % quarters, 2) % dimes, 2)

# Nickels
n_nik = mod_dim // nickels
mod_nik = round(round(round(cash % quarters, 2) % dimes, 2) % nickels, 2)

# Pennies
n_pen = mod_nik // pennies
coins = int(n_qrt + n_dim + n_nik + n_pen)

# Print number of coins to give back
print(coins)