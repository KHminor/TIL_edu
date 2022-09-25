a = [4,5,22,66,3,7899,12,551,23357,23,998]
al = len(a)
for i in range(al):
    mn_idx = i
    for j in range(i+1,al):
        if a[mn_idx]>a[j]:
            mn_idx = j
    a[i],a[mn_idx] = a[mn_idx],a[i]
print(a)