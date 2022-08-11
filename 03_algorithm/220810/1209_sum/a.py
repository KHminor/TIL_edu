a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
c = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i+j == len(a)-1:
            c += a[i][len(a)-1-i]
print(c)