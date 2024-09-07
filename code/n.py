# Ball collide check function
def ballCollide(x1, y1, r1, x2, y2, r2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    centre = dist / 2
    if (centre <= r1+r2):
        return True
    else:
        return False


# Ball 1 co-ordinates and radius
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
r1 = int(input('Enter radius of ball 1: '))
# Ball 2 co-ordinates and radius
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
r2 = int(input('Enter radius of ball 2: '))
# Function call
status = ballCollide(x1, y1, r1, x2, y2, r2)
if status == 1:
    print('Balls are collided')
else:
    print('Balls are not collided')

'''
Output 1:-
Enter x1: 0
Enter y1: 0
Enter radius of ball 1: 1
Enter x2: 5
Enter y2: 5
Enter radius of ball 2: 1
Balls are not collided

Output 2:-
Enter x1: 0
Enter y1: 0
Enter radius of ball 1: 1
Enter x2: 0
Enter y2: 1
Enter radius of ball 2: 1
Balls are collided
'''