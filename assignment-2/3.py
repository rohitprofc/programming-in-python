A = [[1, 2, 3],
     [3, 4, 5],
     [5, 6, 7]]

B = [[1, 2, 1],
     [2, 3, 2],
     [3, 4, 3]]

matrixMul = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

matrixAdd = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

rowsInA = len(A)
rowsInB = len(B)
columnsInA = len(A[0])
columnsInB = len(B[0])

def matrixMultiplication():
    print("Matrix Multiplication")
    if rowsInA == columnsInB:
        for i in range(rowsInA):
            for j in range(columnsInB):
                for k in range(rowsInB):
                    matrixMul[i][j] += A[i][k] * B[k][j]
    else:
        print("Multiplication not possible")
    for ele in matrixMul:
        print(ele)

def matrixAddition():
    print("Matrix Addition")
    for i in range(rowsInA):
        for j in range(columnsInA):
            matrixAdd[i][j] += A[i][j] + B[i][j]
    for ele in matrixAdd:
        print(ele) 
    
matrixMultiplication()
matrixAddition()
'''
Output: -
Matrix Multiplication
[14, 20, 14]
[26, 38, 26]
[38, 56, 38]
Matrix Addition
[2, 4, 4]
[5, 7, 7]
[8, 10, 10]
'''