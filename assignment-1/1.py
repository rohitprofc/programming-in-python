# 1. Write a python program to convert minutes to years and days, input minutes from the user.


noOfMinutes = int(input('Enter no.of minutes: '))
years = (noOfMinutes/(365*24*60))
days = (noOfMinutes/(24*60))
print('Number of years for', noOfMinutes, 'is', years)
print('Number of days for', noOfMinutes, 'is', days)


'''
Output 1:-
Enter no.of minutes: 525600
Number of years for 525600 is 1.0
Number of days for 525600 is 365.0
Output 2:-
Enter no.of minutes: 1
Number of years for 1 is 1.902587519025875e-06
Number of days for 1 is 0.0006944444444444445
'''
