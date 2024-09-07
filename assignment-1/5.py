# 5. Write a python program to print the pattern below.
# Pattern: -
'''
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
'''
for i in range(5):
    for j in range(i+1):
        print('*   ', end='')
    print('\n')
for i in range(4, 0, -1):
    for j in range(i):
        print('*   ', end='')
    print('\n')

'''
Output:-
*   

*   *

*   *   *

*   *   *   *

*   *   *   *   *

*   *   *   *

*   *   *

*   *

*   

'''