def find_it(seq):
    numbers_involved = set(seq)
    if seq == []:
        return None
    elif numbers_involved == 1:
            return number
    else:
        for number in numbers_involved:
            if seq.count(number) % 2 == 1:
                return number
            else:
                continue
