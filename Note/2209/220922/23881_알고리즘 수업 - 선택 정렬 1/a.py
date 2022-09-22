A,K = map(int,input().split())
arr = list(map(int,input().split()))
ch_li = sorted(arr[:])

def selection_sort():
    if :

    else:
        pass


for i in range(A-1,0,-1):
    b_idx = i
    for j in range(i, -1, -1):
        if arr[b_idx] < arr[j]:
            b_idx = j
    arr[i], arr[b_idx] = arr[b_idx], arr[i]

print(arr)