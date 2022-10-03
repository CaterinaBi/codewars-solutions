# Write a code in Python to create a Morse code translator. 
# You can take a string with alphanumeric characters in lower or upper case. 
# The string can also have any special characters as a part of the Morse code. 
# Special characters can include commas, colons, apostrophes, exclamation marks, periods, 
# and question marks. The code should return the Morse code that is equivalent to the string.

def morse_code_translator(s):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', ':', '\'', '!', '.', '?']
    # the space between parts of the same letter is 1 unit
    morse_code_characters = ['. _', '_ . . .', '_ . _ .', '_ . .', '.', '. . _ .', '_ _ .', '. . . .', '. .', '. _ _ _', '_ . _', '. _ . .', '_ _', '_ .', '_ _ _', '. _ _ .', '_ _ . _', '. _ .', '. . .', '_', '. . _', '. . . _', '. _ _', '_ . . _', '_ . _ _', '_ _ . .', ',', ':', '\'', '!', '.', '?']
    morse_code_translation = []

    split_string = s.split()
    # print(split_string)
    
    for word in split_string:
        word = word.lower()
        for letter in word[:-1]:
            index = characters.index(letter)
            morse_code_letter = morse_code_characters[index]
            # the space between letters is 3 units
            morse_code_translation += [ morse_code_letter + '   ' ]
        for letter in word[0:]:
            index = characters.index(letter)
            morse_code_letter = morse_code_characters[index]
            morse_code_translation += morse_code_letter

        # the space between words is 7 units
        morse_code_translation += '       '
    
    return morse_code_translation
                
        
    

# tests
print(morse_code_translator('Will you call me?'))
print(morse_code_translator('Dear, leave me alone!'))
print(morse_code_translator('Don\'t lie to me.'))