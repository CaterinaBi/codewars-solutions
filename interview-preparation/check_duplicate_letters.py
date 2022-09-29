# Write a function in Python to check duplicate letters. 
# It must accept a string, i.e., a sentence. 
# The function should return True if the sentence has any word with duplicate letters, 
# else return False. 

def check_duplicate(s):
    split_container = []
    split_sentence = s.split()
    for word in split_sentence:
        for letter in word:
            if letter in split_container:
                return True
            else:
                split_container += letter
        split_sentence = []
    return False


# tests
print(check_duplicate('Let me tell you something'))
print(check_duplicate('Nothing'))
print(check_duplicate('Call me later'))