# convert decimal numbers to octal numbers

def decimal_to_octal(num):
    num = oct(num)
    return num

# test
print(decimal_to_octal(7)) # should print 7
print(decimal_to_octal(8)) # should print 10
print(decimal_to_octal(16)) # should print 20

# binary

def decimal_to_binary(num):
    num = bin(num)
    return num

# test
print(decimal_to_binary(7)) # should print 0b111
print(decimal_to_binary(8)) # should print 0b1000
print(decimal_to_binary(16)) # should print 0b10000

# hexadecimal

def decimal_to_hexadecimal(num):
    num = hex(num)
    return num

# test
print(decimal_to_hexadecimal(7)) # should print 0x7
print(decimal_to_hexadecimal(8)) # should print 0x8
print(decimal_to_hexadecimal(16)) # should print 0x10