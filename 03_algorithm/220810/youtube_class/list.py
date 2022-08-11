# N = 3   # 행
# M = 4   # 열
# N개의 원소를 갖는 0으로 초기화된 1차원배열
# arr1 = [0]*N

# 크기가 N * M 이고 0으로 쵝화된 2차원 배열    # 2차원 배열 만들때 [0]*열 먼저 하고 * 행하기
# arr2 = [[0]*M]*N # --> 이렇게 만들면 주소 값이 똑같이 복사가 되기 때문에 이렇게 작성하지 말자.
# arr3 = [[0]*M for _ in range(N)]

# arr의 모든 요소를 다 더하는 값 구하기

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
sum = 0
for i in range(N):
    for j in range(N):
        s += N[i][j]
print(sum)