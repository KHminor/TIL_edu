# 0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111
# 00000010001101
li = list(map(int,input().replace(' ','')))

result = []
for i in range(len(li)//7):
    arr = li[i*7:(i+1)*7]
    sum = 0
    # print(arr)
    for j in range(7-1,-1,-1):
        if arr[j]:
            # print(j)
            if j == 6:
                sum += 1
            else:
                sum += 2**(6-j)
    result.append(sum)
print(*result)