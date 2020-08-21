from cs50 import get_string
from sys import argv, exit


def main():
    if len(argv) <= 1 or len(argv) > 2:
        print("Usage: python caesar.py k")
        exit(1)
    ban = argv[1]
    lista = []
    f=open(ban, "r")
    fl = f.readlines()
    for x in fl:
        lista.append(x.strip())
    print("What message would you like to censor?")
    text = get_string("")
    wordlist = text.split()
    bleep_list = []
    for y in range(len(wordlist)):
        for x in range(len(lista)):
            if wordlist[y] == lista[x]:
                temp = "*" * len(wordlist[y])
                wordlist[y] = temp
    print(*wordlist)
    # TODO

if __name__ == "__main__":
    main()
