alpha_li = [chr(i) for i in range(97,123)]
# print(alpha_li)
ch_li = [-1]*26
ip = list(input())
for i in range(len(ip)):
    for j in range(26):
        if ip[i] == alpha_li[j] and ch_li[j] == -1:
            ch_li[j] = i
            break

print(*ch_li)
# # 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# # 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1


# ip = list(input())