def stringLengthCheck(str):
    stringLength = 0
    for i in str:
        i = 0
        if str[i] == '':
            pass
        else:
            stringLength += 1
    print('String length:', stringLength)


def palindromeCheck(str):
    strCheck = str.lower()
    print('Palindrome check:', end=' ')
    if strCheck[0:] == strCheck[-1::-1]:
        print('PALINDROME')
    else:
        print('NOT PALINDROME')


str = input('Enter a string: ')
stringLengthCheck(str)
palindromeCheck(str)

'''
Output 1: -
Enter a string: Rohit
String length: 5
Palindrome check: NOT PALINDROME
Output 2: -
Enter a string: Amma
String length: 4
Palindrome check: PALINDROME
'''
