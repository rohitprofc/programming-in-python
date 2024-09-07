def evenSumOfFibonacci(upto_n):
    evenSum, previousNum, nextNum = 0, 0, 1
    fibonacciList = []
    while(nextNum <= upto_n):
        fibonacciList.append(nextNum)
        if(nextNum % 2) == 0:
            evenSum += nextNum
        previousNum, nextNum = nextNum, previousNum+nextNum
    print('fibonacci list:', fibonacciList)
    print('Sum of even valued numbers in above fibonacci list is: ', evenSum)


upto_n = 10000
evenSumOfFibonacci(upto_n)

'''
Output: -
fibonacci list: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
Sum of even valued numbers in above fibonacci list is:  3382
'''