#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = list(str(number))

a = l[len(l) - 1]
b = int(a)

if b > 5:
  print("Last digit of {} is {} and is greater than 5".format(number, b))
elif b < 6 and b > 0:
  print("Last digit of {} is {} and is less than 6 and greater than 0".format(number, b))
elif b == 0:
  print("Last digit of {} is {} and is 0".format(number, b))
