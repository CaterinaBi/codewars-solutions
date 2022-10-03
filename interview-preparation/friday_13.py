def friday_detector(month, year):
    '''
    A function that accepts to parameters, calculates whether a Friday 13 is in the month,
    and return a bool

    parameters:
    month = int
        two-digit integer indicating the month number
    year = int
        four-digit integer indicating the year number
    '''
    

# tests 
print(friday_detector(5, 2022)) # True
print(friday_detector(10, 2022)) # False
print(friday_detector(6, 2025)) # True