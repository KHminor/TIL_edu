a = [2,4,6,1,9,8,7,0]

# 선택 정렬
for i in range(len(a)-1):
    min_num = i
    for j in range(i,len(a)):
        if a[min_num] > a[j]:
            min_num = j
    a[i],a[min_num] = a[min_num],a[i]

print(a)

#
# def SelectionSort(A,s):
#     global i, ln
#     if i == len(a)-1:
#         return
#     else:
#         min_num = i
#         while i < len(a)
#     pass
# ln = len(a)
# i = 0

def SelectionSort(s):
    n = len(A)
    if s == n-1:
        return
    min = s
    for i in range(s,n):    # 두번째 for문 적용하기
        if A[min] > A[i]:   # 가장 처음 s 와 i의 같은 값은 조건에 부합하지 않기에 넘김
            min = i
    A[s], A[min] = A[min], A[s]
    SelectionSort(s+1)

A = [2,4,6,1,9,8,7,0]
SelectionSort(0)
print(A)