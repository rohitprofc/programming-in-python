# 2.Write a python program to convert Fahrenheit to Celcius and Celcius to Farenheit, user input the value and unit to convert the input unit to the given corresponding unit.


numberValue = int(input('Enter input value: '))
unit = input('Enter unit "F" for Farenheit and "C" for Celcius: ')
convertedValue = 0
if unit.upper() == 'F':
    convertedValue = (numberValue-32)*(5/9)
    print('Value in Celcius is:', convertedValue)
elif unit.upper() == 'C':
    convertedValue = (numberValue*(9/5)) + 32
    print('Value in Farenheit is:', convertedValue)
else:
    print('Enter a valid unit |>""<|')


'''
Output 1:-
Enter input value: 100
Enter unit "F" for Farenheit and "C" for Celcius: c
Value in Farenheit is: 212.0

Output 2:-
Enter input value: 100
Enter unit "F" for Farenheit and "C" for Celcius: f
Value in Celcius is: 37.77777777777778

Output 3:-
Enter input value: 100
Enter unit "F" for Farenheit and "C" for Celcius: s
Enter a valid unit |>""<|
'''
