# 제거후 인벤토리 2초
# 인벤토리에서 꺼내서 블록을 놓는건 1초
# 추가해야할것 해당 블록의 높이 뿐만아니라
# 다른 높이의 블록도 세어볼 필요가 있다는것.

import sys
n,m,b = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# sum(arr,[]) 하면 빈 리스트에 arr요소들을 담을 수 있다. ㄷㄷ
floor = sorted(list(set(sum(arr, []))))
floor.reverse()
mx = max(floor)
mn = min(floor)
# 257(0~256)개에 해당하는 인덱스를 통해 카운팅을 해주기
ch_li = {x:0 for x in range(257)}

# 해당 높이에 대한 개수 카운팅하기
for i in range(n):
    for j in range(m):
        ch_li[arr[i][j]] += 1


# 만약
# 1 4 10
# 1 2 3 4

# 가장 큰 수에서 다른 수(ex) 3이면 3*value)들을 뺀 합이 b 보다 같거나 작다면 가능
# 만약에 크다면 제외를 해야한다.
# 제외를 한다면 두번째로 큰 수에서 다른 수들을 뺀 합 (큰 값이 있을 경우엔 절댓값의 *2)이 b보다 작다면 가능

result = []

for i in range(mn,mx+1):
    hab = 0
    block = b
    for j in range(len(floor)):
        if i == floor[j]: pass
        elif i > floor[j]:
            hab += ch_li[floor[j]] * (i - floor[j])
            block -= ch_li[floor[j]]

        else:
            hab += 2*-(ch_li[floor[j]] * (i - floor[j]))
            block += ch_li[floor[j]]


    if block >= 0:
        result.append([hab,i])

result.sort(key=lambda x: (x[0]))
result2 = result[0]
for i in range(1,len(result)):
    if result2[0] == result[i][0] and result[i][1] > result2[1] :
        result2 = result[i][1]

print(result)
print(*result2)

# 3 4 11
# 29 51 54 44
# 22 44 32 62
# 25 38 16 2

# 4 4 36
# 15 43 61 21
# 19 33 31 55
# 48 63 1 30
# 31 28 3 8


# 3 4 64
# 0 0 0 0
# 0 0 0 0
# 0 0 0 64

# 3 4 1
# 64 64 64 64
# 64 64 64 64
# 64 64 64 63