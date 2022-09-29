def reverse_number(n):
    # convert int to string
    number = str(n)
    reverse_num = ''        
    # reverse number
    if len(number) == 1:
        return n
    else:
        for char in number:
            reverse_num = char + reverse_num
        # check whether number is negative
        if number[0] == '-':
            reverse_num = reverse_num[:-1]
            reverse_num = '-' + reverse_num
        # convert string back to int
        reverse_num = int(reverse_num)
        return reverse_num
