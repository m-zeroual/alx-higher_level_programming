#!/usr/bin/python3
a = 'a'
while True:
    print("{}".format(a), end = "")
    if a == 'z':
        break
    a = chr(ord(a) + 1)
