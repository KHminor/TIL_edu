def partition(l,r):
    pivot = li[l]
    i,j = l+1,r
    while i<=j:
        while i<=j and li[i] <= pivot: # 피봇보다 작거나 같을 경우
            i += 1
        while i<=j and li[j] >= pivot:  # 피봇보다 크거나 같을 경우
            j -= 1
        if i < j:
            li[i],li[j] = li[j],li[i]
    li[l],li[j] = li[j],li[l]
    return j        # j를 리턴하는 이유는 해당 위치를 기준으로 정렬을 위해

def p_sort(l,r):
    if l < r:
        s = partition(l,r)
        p_sort(l,s-1)
        p_sort(s+1,r)





n = 10
li = [7,5,4,1,2,10,3,6,9,8]
p_sort(0,n-1)
print(li)