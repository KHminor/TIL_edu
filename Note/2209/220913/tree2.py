def pre(n):
    if n <= size:
        print(tree[n] , end=' ')
        pre(2*n)
        pre(2*n+1)

def ino(n):
    if n <= size:
        ino(2*n)
        print(tree[n], end= ' ')
        ino(2*n+1)

def post(n):
    if n <= size:
        post(2*n)
        post(2*n+1)
        print(tree[n], end=' ')

tree = [0, 'A', 'B', 'C', 'D', 'E', 'F'] # 완전이진트리
size = len(tree) -1 # 마지막 정점 번호

pre(1)
print()
ino(1)
print()
post(1)