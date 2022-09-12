# def duplicated_letters(s):
#     pass
#     li = []
#     for i in range(len(s)):
#         for j in range(i+1,len(s)):
            # if s[i] == s[j]:
            #     if s[i] not in li:
#                     li.append(s[i])
    
#     return li


# print(duplicated_letters('apple')) # => [‘p’]
# print(duplicated_letters('banana')) # => [’a’, ‘n’]


# def low_and_up(s):
#     pass
#     s = s.lower()
#     st = []
#     st.append(s[0])
#     up_s = ''
#     for i in range(1,len(s)):
#         if i % 2 != 0:
#             up_s = s[i].upper()
#             st.append(up_s)
#         else:
#             st.append(s[i])
#     st = ''.join(st)
#     return st

# print(low_and_up('apple')) # => aPpLe
# print(low_and_up('banana')) # => bAnAnA


def lonely(list):
    pass
    remove_li = []
    for i in range(1,len(list)):
        if list[i] != list[i-1]:
                remove_li.append(list[i-1])
        if i+1 == len(list):
            remove_li.append(list[i])
    return remove_li

print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) # => [4, 3]
