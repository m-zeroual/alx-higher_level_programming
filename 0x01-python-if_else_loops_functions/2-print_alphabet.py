#!/usr/bin/python3
a = 'a'
while True:
    print(f"{a}", end = '')
    if a == 'z':
        break
    a = chr(ord(a) + 1)
