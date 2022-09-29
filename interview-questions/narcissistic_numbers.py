# An n digit number is narcissistic if the sum of its digits 
# to the nth power equal the original number.

def narcissistic(value):
    # convert into string
    value_string = str(value)
    value_length = len(value_string)
    result_number = 0
    
    for char in value_string:
        char = int(char)
        result_number += char**(value_length)
        # check if result equals original number
    if result_number == value:
        return True
    else:
        return False
