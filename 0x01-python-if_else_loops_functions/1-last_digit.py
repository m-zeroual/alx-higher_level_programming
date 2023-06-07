#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(str(number)[-1])
if number < 0:
    last_num = -last_num
if last_num < 6 and last_num != 0:
    print(f"Last digit of {number:d} is {last_num:d} and is less than 6 and not 0")
elif last_num > 5:
    print(f"Last digit of {number:d} is {last_num:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last_num:d} and is 0")
