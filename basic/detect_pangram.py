import string

def is_pangram(s):
    # input_string = input()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in letters:
        if letter not in s.lower():
            return False
        else:
            continue
    return True
