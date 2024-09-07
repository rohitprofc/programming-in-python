class student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def readmarks(self):
        print('Enter', name, '3 subjects marks:')
        for i in range(3):
            ele = int(input())
            self.marks.append(ele)

    def displaydata(self):
        print('Student name:', self.name)
        print('Student marks:', self.marks)
        print('Sum of Student marks:', sum(self.marks))
        print('Avg of Student marks:', sum(self.marks)/len(self.marks))


name = input('Enter student name:')
obj = student(name)
obj.readmarks()
obj.displaydata()
'''
Output: -
Enter student name:Rohit
Enter Rohit 3 subjects marks:
98
99
97
Student name: Rohit
Student marks: [98, 99, 97]
Sum of Student marks: 294
Avg of Student marks: 98.0
'''
