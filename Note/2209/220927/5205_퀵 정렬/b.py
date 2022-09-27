# 돌아와서 퀵 정렬 다시 한번 더 작성해보기
def partition(l,r):
    global n
    pivot = li[l]
    i,j = l+1,r
    while i <=j:
        while i<=j and li[i] <= pivot:
            i +=1
        while i<=j and li[j] >= pivot:
            j -=1
        if i < j:
            li[i],li[j] = li[j],li[i]

    li[l],li[j] = li[j],li[l]
    return j

def p_sort(l,r):
    if l < r:
        s = partition(l,r)
        p_sort(l,s-1)
        p_sort(s+1,r)


li = [3,4,2,5,99,6,48,7]
n = len(li)
p_sort(0,n-1)
print(li)
