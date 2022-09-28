'''
6 8     V :마지막 정점번호(0번부터 시작), E :간선의 수
0 1 0 2 0 5 0 6 6 4 4 3 5 3 5 4
'''
V,E = map(int,input().split())
arr = list(map(int,input().split()))
# 인접 행렬
li = [[0]*(V+1) for _ in range(V+1)]
# 연결 리스트
li_2 = [[] for _ in range(V+1)]
for i in range(E):
    a,b = arr[i*2],arr[i*2+1]
    li[a][b] = 1
    li[b][a] = 1        # 이 줄은 방향이 없는 경우에만 적용

    li_2[a].append(b)
    li_2[b].append(a)   # 이 줄은 방향이 없는 경우에만 적용

print(li)
print(li_2)