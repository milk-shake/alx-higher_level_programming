import random
number = random.randint(-10, 10)
print(number, "is positive" if number > 0 else "is negative",end="\n")