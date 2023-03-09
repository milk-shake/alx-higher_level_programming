#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)


def check(number):
    if (abs(number % 10)) > 5:
        x = print("and is greater than 5")
    elif (abs(number % 10)) == 0:
        x = print("and is 0")
    elif (abs(number % 10)) < 6 and not 0:
        x = print("and is less than 6 and not 0")


# print(f"Last digit of", number, "is", (abs(number % 10)), check(number))


def check2():
    num_string = str(number)
    num_len = len(num_string)
    below_zero = number < 0 and abs(number) % 10 != 0
    print(f"Last digit of {number} is {'-' if below_zero else ''}{num_string[num_len - 1 :]}{' and is greater than 5' if (abs(number) % 10) > 5 else ''}{' and is 0' if (abs(number) % 10 == 0) else ''}{' and is less than 6 and not 0' if ((abs(number) % 10 < 6) and not 0) else ''}")


# check2()

def check3():
    our_string = ""