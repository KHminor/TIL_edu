n  = 3
a = [1,2,3,4,5]
for i in range(1<<n):
    for j in range(len(a)):
        if i & (1<<j):
            print(a[j], end=' ')
    print()