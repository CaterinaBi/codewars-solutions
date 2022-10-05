# convert decimal numbers to octal numbers

def decimal_to_octal(num):
    num = oct(num)
    return num

# test
print(decimal_to_octal(7)) # should print 7
print(decimal_to_octal(8)) # should print 10
print(decimal_to_octal(16)) # should print 20