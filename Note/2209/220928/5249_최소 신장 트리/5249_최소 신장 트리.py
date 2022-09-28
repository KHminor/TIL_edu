import sys
sys.stdin = open('sample_input (3).txt')

def findset(x):
    if x == parent[x]:      # 자기 자신을 바라보고 있다면
        return x
    else:
        return findset(parent[x])
        

def mst():
    cnt = 0         # 간선의 개수
    result = 0      # 전체 가중치의 합
    idx = 0         # 조사 대상 idx
    # MST 구성하는 반복문
    while cnt < v:    # 사이클 없는 트리의 간선의 개수는 v-1
        p1 = findset(arr[idx][0])
        p2 = findset(arr[idx][1])
        # 사이클이 형성되지 않을 때
        if p1 != p2:
            # arr 는 가중치 기준으로 오름차순 정렬 하였으므로 일단 삽입
            result += arr[idx][2]   # idx 번째 정보의 n1,n2사이의 간선 잇기
            cnt += 1        # 간선 개수 하나 증가
            parent[p2] = p1
        idx += 1
    return result
            
        
        
T = int(input())

for tc in range(1,T+1):
    v,e = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(e)]
    arr.sort(key=lambda x: x[2])
    
    parent = list(range(v+1))
    print(mst())