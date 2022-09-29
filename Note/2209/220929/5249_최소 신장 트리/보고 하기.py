from pprint import pprint
# 여기서 parent 를 사용하는 이유는 해당 노드들이
# 같은 노드를 부모로 두고 있는지 체크할 수 있다.
import sys
sys.stdin = open('sample_input (7).txt')
def findset(x):
    if x == parent[x]: return x
    else: return findset(parent[x])

def mst():
    cnt = result = idx = 0
    while cnt < v:
        p1 = findset(arr[idx][0])
        p2 = findset(arr[idx][1])
        if p1 != p2:
            result += arr[idx][2]
            cnt += 1
            parent[p2] = p1
        idx += 1
    return result

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(e)]
    arr.sort(key=lambda x:x[2])

    parent = list(range(v+1))
    # print(parent)
    # pprint(arr)
    result = mst()
    print(f'#{tc} {result}')