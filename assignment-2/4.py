f = open("C:\\Users\\Rohit Chess\\Desktop\\Python-Programming\\Assignment - 2\\example.txt", "r")

noOfVowels = 0
noOfConsonants = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for alpha in f.read():
    if alpha in vowels:
        noOfVowels += 1
    elif alpha not in vowels and alpha != '\n':
        noOfConsonants += 1


print("No.of vowels in = ", noOfVowels)
print("No.of consonants in = ", noOfConsonants)
'''
Output: -
No.of vowels in =  15
No.of consonants in =  24
'''