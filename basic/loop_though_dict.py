# declare dictionary, method 1
dict1 = dict(martina=30, billy=32, oreste=1)
print(dict1)

# declare dictionary, method 2
dict2= {'caterina': 36, 'vincent': 42, 'isadora':5, 'leone':2}
print(dict2)

# get fist element
print(dict2['caterina'])

# print keys
for x in dict2.keys():
    print(x)

for y in dict2.values():
    print(y)

# adds element
dict2['carmen'] = 61
print(dict2)

# deletes element
del dict2['carmen']
print(dict2)

# loops through keys and values
for x, y in dict2.items():
    print(x, y)