N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# for i in range(N): # 0.0, 1.1, 2.2, 3.3 의 값 출력
#     for j in range(N):
#         if i == j:
#             print(arr[i][j])

# 또는
# print([arr[i][i] for i in range(N)])

# ========================================================

for i in range(N):  # 반대 대각선 구하기
    s += arr[i][N-1-i]
