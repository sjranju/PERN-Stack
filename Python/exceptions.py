import sys

try:
    res = 0/0
    print('result is', res)
except ZeroDivisionError:
    print('You cant divide by 0')
   
try: 
    number = int(input('Enter a number between 1-10: '))
except ValueError:
    print('Please enter number, not string/text')
    sys.exit()

print('You entered',number)