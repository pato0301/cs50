from cs50 import get_string, sys
#print(len(sys.argv[1]))
#print(type(sys.argv[1]))
if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print("Usage: python caesar.py k")
    sys.exit(1)
key = int(sys.argv[1])
text = get_string("plaintext: ")
print("ciphertext: ", end="")
for i in range(len(text)):
    if text[i].isalpha():
        #print(text[i])
        if text[i].isupper():
            #print(text[i])
            letter = ord(text[i]);
            result = (((((letter -65) + key) % 26) + 65))
            print(chr(result), end="")
        elif text[i].islower():
            #print(text[i])
            letter = ord(text[i])
            result = ((((letter -97) + key) % 26) + 97)
            print(chr(result), end="")
    else:
        print(text[i], end="")
print("")
#print(int(sys.argv[1]))