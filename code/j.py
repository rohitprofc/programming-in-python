from ArithmeticPackage import ArithmeticDemo

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print('\nSum of two number is:', end='  ')
print(ArithmeticDemo.sumtwo(a, b))
print('\nSubstraction of two number is:', end='  ')
print(ArithmeticDemo.subtwo(a, b))
print('\nProduct of two number is:', end='  ')
print(ArithmeticDemo.multwo(a, b))
print('\nDivision of two number is:', end='  ')
print(ArithmeticDemo.divtwo(a, b))

'''
Output: -
Enter a: 4
Enter b: 5

Sum of two number is:  9

Substraction of two number is:  -1

Product of two number is:  20

Division of two number is:  0.8
'''