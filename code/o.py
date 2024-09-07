from statistics import mean, median, mode


lst = []
noOfElements = int(input("Enter no.of elements: "))
for i in range(noOfElements):
    ele = int(input("Enter element "+str(i+1)+": "))
    lst.append(ele)

print("List:", lst)
print("Mean of given list: ", mean(lst))
print("Median of given list: ", median(lst))
print("Mode of given list: ", mode(lst))

'''
Output: -
Enter no.of elements: 4
Enter element 1: 4
Enter element 2: 5
Enter element 3: 5
Enter element 4: 1
List: [4, 5, 5, 1]
Mean of given list:  3.75
Median of given list:  4.5
Mode of given list:  5
'''
