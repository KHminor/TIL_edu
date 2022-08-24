arr = [list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(4):
        print(arr[i][j + (4-1-2*j) * (i%2)])
