'''
정점 번호 V : 1~(E+1)
E = 간선 수
부모-자식 순
4
2 1 2 3 1 4 1 5
'''

def find_root(V):   # 루트 찾기
    for i in range(1, V + 1):
        # 부모가 없으면 root
        if par[i] == 0:
            return i

E = int(input())
arr = list(map(int,input().split()))
V = E + 1


# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1) # 좌측
ch2 = [0]*(V+1) # 우측

# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

# 간선의 수만큼 반복
for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

# 현재 루트는 모르는 상태
root = find_root(V)
print(root)
print(par)

