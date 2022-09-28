import string

def is_isogram(string):
    checked_letters = []
    if string == '':
            return True
    for letter in string.lower():
        if letter not in checked_letters:
            checked_letters.append(letter)
        else:
            return False
    return True
