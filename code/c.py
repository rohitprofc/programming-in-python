# Distance between two points using pythagorean theorem

print('Enter two points A(x1,y1) & B(x2,y2) to find distance between them')
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
dist = (((x2-x1)**2)+((y2-y1)**2))**0.5
print(dist)

'''
Output:-
Enter two points A(x1,y1) & B(x2,y2) to find distance between them
Enter x1: 0
Enter y1: 0
Enter x2: 5
Enter y2: 5
7.0710678118654755
'''
