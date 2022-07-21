
a = [1, 1, 3, 3, 0, 1, 1]

for i in range(len(a)):
    cnt = i +1
    if cnt < len(a):
        if a[i] == a[cnt]:
            del a[i]

print(a)
