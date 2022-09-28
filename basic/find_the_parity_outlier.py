def find_outlier(integers):
    odd_array = []
    even_array = []
    for number in integers:
        if number % 2 == 1:
            odd_array.append(number)
        else:
            even_array.append(number)
    if len(odd_array) == 1:
        return odd_array[0]
    elif len(even_array) == 1:
        return even_array[0]
