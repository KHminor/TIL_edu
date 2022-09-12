# numbers = [7, 10, 22, 4, 3, 17]
# max_num = numbers[0]

# for i in numbers:
#     if i > max_num:
#         max_num = i
# print(max_num)

# =================================
# min_num = numbers[0]
     
# for i in numbers:
#     if i < min_num:
#         min_num = i
# print(min_num)

# =================================
# numbers = [7, 10, 22, 7, 22, 22]
# cnt = 0
# max_num = numbers[0]

# for i in numbers:
#     if max_num == i:
#         cnt += 1
#     if i > max_num:
#         max_num = i
# print(max_num, cnt)

# 'a' 가 싫어

# word = input()

# result = ''
# for i in word:
#     print(i)
#     if i == "a":
#         continue
#     result += i
# print(result)


# word = input()
# word.replace('a', '')

# ===================================

# 단어 뒤집기

word = input()

result = ''
# apple

for i in word:
    result = i + result

print(result)