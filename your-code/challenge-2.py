""" To import random library in the global scope it is more efficient than applying it to every local function"""
import random

"""For clarity sake the letters and numbers that can be chosen in the string are listed below and then passed by the name in the function"""

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def RandomStringGenerator(min_length, length=12):
    counter = 0
    string = ''
    while counter < length:
        string += random.choice(min_length)
        counter += 1
    return string

def BatchStringGenerator(num_strings, min_length=8, max_length=12):
    res = []
    for i in range(num_strings):
        c = None
        if min_length < max_length:
            c = random.choice(range(min_length, max_length))
        elif min_length == max_length:
            c = min_length
        else:
            return('Incorrect min and max string lengths. Try again.')   #shortened without need of importing a library
        res.append(RandomStringGenerator(char, c))                      #an argument is added to call the list strings
    return res

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))