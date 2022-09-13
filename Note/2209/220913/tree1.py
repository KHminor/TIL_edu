'''
정점 번호 V : 1~(E+1)
E = 간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def preorder(n):    # 전위 순회
    if n:           # n 이 0이 아니면
        print(n)    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):    # 중위 순회
    if n:           # n 이 0이 아니면
        inorder(ch1[n])
        print(n)    # visit(n)
        inorder(ch2[n])

def postorder(n):   # 후위 순회
    if n:           # n 이 0이 아니면
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)    # visit(n)

E = int(input())
arr = list(map(int,input().split()))
V = E + 1
root = 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1) # 좌측
ch2 = [0]*(V+1) # 우측

# 간선의 수만큼 반복
for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c

print(ch1)
print(ch2)

preorder(root)
print('='*10)
inorder(root)
print('='*10)
postorder(root)
# 둘다 사용 가능
# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j+1]