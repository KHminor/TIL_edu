import sys
sys.stdin = open('sample_input (6).txt')

def find_set(x):
    if x == visited[x]: return x
    else: return find_set(visited[x])

T = int(input())
# n = 출석 번호 수, m = 신청서 수
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [i for i in range(n+1)]
    result = []
    for i in range(m):
        p,c = arr[i*2],arr[i*2+1]
        visited[c] = p
    print(visited)
    for i in range(1,n+1):
        f = find_set(visited[i])
        if f not in result:
            result.append(f)

    result = len(result)
    print(f'#{tc} {result}')

