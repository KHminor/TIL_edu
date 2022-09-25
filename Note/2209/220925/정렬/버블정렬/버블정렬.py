a = [4,5,22,66,3,7899,12,551,23357,23,998]
al = len(a)
for i in range(al-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1]= a[j+1],a[j]

print(a)



