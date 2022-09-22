import sys
A,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
ch_li = sorted(arr[:])
cnt = 0
result = 1
for i in range(A-1,0,-1):
    if arr == ch_li and cnt == K:
        break

    b_idx = i

    for j in range(i-1,-1,-1):
        if arr[b_idx] < arr[j]:
            b_idx = j

    if arr[i] == arr[b_idx]:
        continue

    arr[i],arr[b_idx] = arr[b_idx],arr[i]
    cnt += 1

    if arr == ch_li and cnt < K:
        result = -1
        break

    elif cnt == K:
        break

# 경우1 : k보다 정렬이 먼저 된 경우
# 경우2 : 정렬이 되기 전에 cnt == k 의 경우

if result == -1:
    print(result)
else:
    print(arr[b_idx], arr[i])