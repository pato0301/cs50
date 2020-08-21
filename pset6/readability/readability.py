# Import Library
from cs50 import get_string
import re

# Ask for text input
text = get_string("Text: ")

# Obtengo el numero de oraciones
sent_num = max(len(re.split('! |\? |\. ', text)), 0)

# Get number of words in text
text_split = text.split()
num_words = len(text_split)

# Get all the letter
res = re.findall(r'\w+', text)
letras_cant = res
letras = 0

# Loop through each word
for word in res:
    cant = len(word)
    letras = letras + cant

# Calculate Coleman-Liau index
avg_let = ((letras) / num_words) * 100
avg_sent = ((sent_num) / num_words) * 100

level = round((0.0588 * avg_let) - (0.296 * avg_sent) - 15.8)

# Get Grade to Level
if level < 1:
    print('Before Grade 1')
elif level > 16:
    print('Grade 16+')
else:
    print('Grade', level)