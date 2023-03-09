#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        n = ord(str[s])
        if n >= 97 and n <= 122:
            n -= 32
        print("{}".format(chr(n)), end="")
    print()
