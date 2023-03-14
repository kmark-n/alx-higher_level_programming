#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for str in range(len(sys.argv)):
        if str == 0:
            continue
        else:
            result += int(sys.argv[str])
        print("{}".format(result))
