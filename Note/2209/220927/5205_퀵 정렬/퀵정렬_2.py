def partition(l,r):
    pivot = li[l]
    i,j = l,r
    while i<=j:
        while i<=j and li[i] <= pivot:
            i +=1
        while i<=j and li[j] >= pivot:
            j -=1
        if i<j:
            li[i],li[j] = li[j],li[i]
    li[l],li[j] = li[j],li[l]
    return j

def p_sort(l,r):
    if l < r:
        s = partition(l,r)
        p_sort(l,s-1)
        p_sort(s+1,r)


li = [3,487,4,5,766,89,55,66,12,12,3,4]
ln = len(li)
p_sort(0,ln-1)
print(li)

# 다 외웠다!!
