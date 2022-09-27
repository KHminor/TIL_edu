def partition(l,r):
    pivot = A[l]
    i,j = l,r
    while i<=j:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i < j:
                A[i], A[j] = A[j], A[i]
    A[i], A[j] = A[j], A[i]
    return j

def qsort(l,r):
    if l < r:
        s = partition(l,r)
        qsort(l, s-1)
        qsort(s+1,r)

A = [7,2,5,3,4,5]