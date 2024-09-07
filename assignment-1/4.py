# 4. Write a program to enter a number and display its Hexadecimal and octal equivalent and its square root.
from math import sqrt


number = int(input('Enter a number: '))
print('Hexadimal equivalent of input number is',hex(number))
print('Octal equivalent of input number is',oct(number))
print('Square root of input number is',sqrt(number))

'''
Output 1:-
Enter a number: 51
Hexadimal equivalent of input number is 0x33
Octal equivalent of input number is 0o63
Square root of input number is 7.14142842854285

Output 2:-
Enter a number: 45
Hexadimal equivalent of input number is 0x2d
Octal equivalent of input number is 0o55
Square root of input number is 6.708203932499369
'''