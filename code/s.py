f  = open("C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Lab Programs\\myfile.txt","r")
for line in f:
    print(line.strip()[::-1])
f.close()
'''
Output: -
Hello,
My name is Rohit
I play chess
A game??
'''