# Displaying grade of student obtained by 5 subjects marks
from numpy import average


subject = []
name = input('Enter student name: ')
for i in range(5):
    marks = int(input("Enter marks of subject "+str(i+1)+": "))
    subject.append(marks)

avg = average(subject)
print('Grade of', name, 'is:', end=' ')
if avg >= 90:
    print('O')
elif avg >= 80:
    print('A+')
elif avg >= 70:
    print('A')
elif avg >= 60:
    print('B+')
elif avg >= 50:
    print('B')
elif avg >= 40:
    print('C')
else:
    print('F')

'''
Output:-
Enter student name: Monty Python
Enter marks in subject 1: 98
Enter marks in subject 2: 96
Enter marks in subject 3: 94
Enter marks in subject 4: 92
Enter marks in subject 5: 95
Grade of Monty Python is:
O
'''
