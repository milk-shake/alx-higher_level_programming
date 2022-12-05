#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number, "is positive" if number > 0 else "is negative",end="\n")