def dict_invert(my_dict):
    pass
    value = my_dict.keys()
    key = my_dict.values()
    value_li = []
    new_dict = {}
    for i in value:
        value_li.append(i)
    print(value_li)
    for i in  key:
        for j in range(len(value_li)):
            if i == True:
                new_dict[True] = value_li
                break
            else: 
                new_dict[i] = [value_li[j]]
           
    return new_dict


print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))

