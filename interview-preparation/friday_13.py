from calendar import month_name


def friday_detector(month, year):
    '''
    A function that accepts two parameters, calculates whether a Friday 13 is in the month,
    and return a bool

    parameters:
    month = int
        one/two-digit integer indicating the month number
    year = int
        four-digit integer indicating the year number
    '''

    day_names = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    month_length = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    year = list(len(1772, 2051))

    
    month = 1
    # 1752 was first leap year
    year = 1752

    dict = {'Year': 1752, 'Month': 1, 'Day': 1, 'Name': day_names[5]}

    for day in day_names:
        day = 1
        day_name = day_names[5]

# tests 
print(friday_detector(5, 2022)) # True
print(friday_detector(10, 2022)) # False
print(friday_detector(6, 2025)) # True