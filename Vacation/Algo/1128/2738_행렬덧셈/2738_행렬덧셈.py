import sys

a,b = map(int,sys.stdin.readline().split())

arrA = [list(map(int,sys.stdin.readline().split())) for _ in range(a)]
arrB = [list(map(int,sys.stdin.readline().split())) for _ in range(a)]


for i in range(a):
    for j in range(b):
        print(arrA[i][j] + arrB[i][j], end=' ')
    print()

