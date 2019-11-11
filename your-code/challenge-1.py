"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

"The two functions defined below print the warning message if the inputs are not correct"

def correct_let (let, num):
    if let not in num:
        print("I am not able to answer this question. Check your input.")

def correct_op ():
    if b != 'minus' and b != 'plus':
        print("I am not able to answer this question. Check your input.")

"This funcion turns the input written numbers into integers and thus make more efficent the maths of the function 'calcfun'"

def convert (w_num):
    if w_num in dic.keys():
        return dic.get(w_num)

"This function builds the logic of the calculator math"

def calcfunc (first, operator, second):
    if operator == 'minus':
        print(f'{first} {operator} {second} equals {first-second}')
    else:
        print(f'{first} {operator} {second} equals {first+second}')

"""'dic' is the dictionary used to convert written numbers to integers. 
'numbers' is the list used to check whether imputs comply with what is expected"""

dic = {'zero': 0, 'one':1, 'two':2,'three':3,'four':4,'five':5}
numbers = ('zero', 'one', 'two','three','four','five')

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')


a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

"""Here are placed the calls of the functions"""
correct_let(a, numbers)
correct_let(c, numbers)

a = convert(a)
c = convert(c)

calcfunc(a, b, c)

correct_op()

print("Thanks for using this calculator, goodbye :)")
