a = int(input('Enter a: '))
b = int(input('Enter b: '))
userList = [1,2,3,4,5]
try:
    c = a/b
    print("Division(a/b): ",c)
    print(userList[3])
except(ZeroDivisionError,IndexError):
    print("Go and check try block there may be error in Division or Index")
else:
    print("No execption")
finally:
    print("END")

'''
Output 1: -
Enter a: 4
Enter b: 5
Division(a/b):  0.8
Go and check try block there may be error in Division or Index
END

Output 2: -
Enter a: 5
Enter b: 1
Division(a/b):  5.0
4
No execption
END
'''