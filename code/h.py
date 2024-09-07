def cumulativeProduct(userList):
    print('Cumulative product of given list is:')
    pro = 1
    for ele in userList:
        pro *= ele
        print(pro)


numberOfElements = int(input('Enter number of elements in the list: '))
userList = []
for evEle in range(numberOfElements):
    inEle = int(input('Enter number: '))
    userList.append(inEle)
cumulativeProduct(userList)

'''
Output: -
Enter number of elements in the list: 5
Enter number: 15
Enter number: 23
Enter number: 45
Enter number: 51
Enter number: 69
Cumulative product of given list is:
15
345
15525
791775
54632475
'''