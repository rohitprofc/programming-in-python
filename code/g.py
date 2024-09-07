# Write a program to find sum of all prime numbers upto 100

sum = 2

for num in range(3, 100):

    i = 2

    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            break

    if i is not num:
        sum += num

print('Sum of all prime numbers upto 100 is', sum)

# Output:- Sum of all prime numbers upto 100 is 1060
