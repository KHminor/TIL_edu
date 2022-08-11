N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
r_sum = l_sum = 0

for i in range(N):
    for j in range(N):  # 열
        if j < i :
            r_sum += arr[i][j]
        elif j > i:
            l_sum += arr[i][j]
print(l_sum, r_sum)


# for i in range(N):
#     for j in range(i+1, N):
#         r_sum += arr[i][j]