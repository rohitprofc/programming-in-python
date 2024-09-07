f = open("C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Assignment - 2\\example.txt", "r")

noOfLines = 0
noOfCharacters = 0

for alpha in f.read():
    if alpha not in "" and alpha != '\n':
        noOfCharacters += 1
    elif alpha == '\n':
        noOfLines += 1

print("No.of Lines in = ", noOfLines)
print("No.of Characters in = ", noOfCharacters)
'''
Output: -
No.of Lines in =  2
No.of Characters in =  39
'''