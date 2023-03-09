#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        n = ord(str[s])
        if n >= 65 and n <= 90:
            n -= 32
        print("{}".format(chr(n)), end="")
    print()
