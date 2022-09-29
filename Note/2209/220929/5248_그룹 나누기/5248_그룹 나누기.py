import sys
sys.stdin = open('sample_input (6).txt')
T = int(input())
# n = 출석 번호 수, m = 신청서 수
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [i for i in range(n+1)]
    cnt = 0
    for i in range(m):
        p,c = arr[i*2],arr[i*2+1]
        visited[c] = p

    for j in range(1,n+1):
        if j == visited[j]:
            cnt += 1
    # print(visited)
    print(f'#{tc} {cnt}')

# 나와있는 케이스는 다 맞는데 틀림