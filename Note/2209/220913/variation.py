'''
정점 번호 V : 1~(E+1)
E = 간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def preorder(n):    # 전위 순회
    global cnt
    if n:           # n 이 0이 아니면
        cnt += 1
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

def f(n):           # global cnt 없이 순회한 정점의 수 리턴하는 함수.
    if n == 0:      # 서브트리가 비어있으면 즉 자식이 없으면
        return 0
    else:           # 자식이 있으면
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

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

# print(ch1)
# print(ch2)
cnt = 0
preorder(root)
# print(cnt)
# print('='*10)
# inorder(root)
# print('='*10)
# postorder(root)
print('='*10)
print(f(3))
