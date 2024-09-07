from math import gcd

a = int(input('Enter a:'))
b = int(input('Enter b:'))
print('GCD of a and b is: ', end='  ')
print(gcd(a, b))
print('LCM of a and b is: ', end='  ')
print((a*b//gcd(a, b)))


'''
Output 1: -
Enter a:4
Enter b:5
GCD of a and b is:   1
LCM of a and b is:   20

Output 2: -
Enter a:5
Enter b:1
GCD of a and b is:   1
LCM of a and b is:   5
'''