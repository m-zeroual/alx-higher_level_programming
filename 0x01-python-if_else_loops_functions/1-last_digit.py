#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(str(number)[-1])
if number < 0:
    print(f"Last digit of {number} is {-last_num} ", end = '')
else:
    print(f"Last digit of {number} is {last_num} ", end = '')
if last_num < 6:
    print("and is less than 6 and not 0")
elif last_num > 5:
    print("and is greater than 5")
else:
    print("and is 0")
