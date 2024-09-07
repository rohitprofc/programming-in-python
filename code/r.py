class ShortInputException(Exception):
    def __init__(self, length):
        Exception(self)
        self.len = length


string = input("Enter the string: ")
length = len(string)
try:
    if length < 3:
        raise ShortInputException(length)
except ShortInputException as s:
    print("The length is string is 3 or greater than 3 but your entered string length is", s.len)
else:
    print("No Exection proceed")
'''
Output 1: -
Enter the string: Rohit
No Exection proceed
Output 2: -
Enter the string: Hi
The length is string is 3 or greater than 3 but your entered string length is 2
'''
