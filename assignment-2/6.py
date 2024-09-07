f1 = open("C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Assignment - 2\\example.txt", "r")
f2 = open("C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Assignment - 2\\filecopy.txt", "a")

for line in f1:
    f2.write(line)
    print("Copy Successful")
'''
Output: -
Copy Successful
Copy Successful
'''