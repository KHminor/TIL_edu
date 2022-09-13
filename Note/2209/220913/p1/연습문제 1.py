'''
정점의 수 : 13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(n):
    if n:
        print(n , end=' ')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(n , end=' ')
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n , end=' ')

V = int(input())
arr = list(map(int,input().split()))
print(arr)
print('='*60)
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
root = 1
# 간선의 수
E = V-1
for i in range(E):
    p,c = arr[i*2], arr[i*2+1]
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c
print(ch1)
print('='*50)
print(ch2)

preorder(root)
print()
inorder(root)
print()
postorder(root)