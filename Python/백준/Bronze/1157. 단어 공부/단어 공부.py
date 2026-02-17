array = input()
array_dict2 = dict()
array = array.upper()
for i in array:
    if i in array_dict2:
        array_dict2[i] += 1
    else:
        array_dict2[i] = 1

max_value = max(array_dict2.values())
result = ""
for i in array_dict2:
    if max_value == array_dict2.get(i):
        if result != "":
            result = "?"
            break
        result = i

print(result)