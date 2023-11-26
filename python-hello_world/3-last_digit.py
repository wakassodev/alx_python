#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[:-1] > 5: 
    print("Last digit of {number} is {number[:-1]} and is lest than 5")
elif number[:-1] == 0: 
    print("Last digit of {number} is {number[:-1]} and is 0")
elif number[:-1] <6 and number[:-1] != 0: 
    print("Last digit of {number} is {number[:-1]} and is less than 6 and not 0")