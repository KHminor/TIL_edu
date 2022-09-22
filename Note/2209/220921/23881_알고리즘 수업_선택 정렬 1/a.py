# A: 배열 크기, K: 교환 횟수
A,K = map(int,input().split())
# K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다.
# 교환 횟수가 K보다 작으면 -1

arr = list(map(int,input().split()))
ch_li = sorted(arr[:])
cnt = y = l = 0
flag = 'True'
result = 1
for i in range(A-1,0,-1):
    if arr == ch_li and cnt == K:
        break
    b_idx = i
    for j in range(i,-1,-1):
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

if result == -1:
    print(result)
else:
    print(arr[b_idx], arr[i])
