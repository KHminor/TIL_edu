import sys
sys.stdin = open('sample_input.txt')
# N : 집합 A안에 있는 1~12 의 숫자 중 몇개를 뽑을 것인지.
# K : N개를 뽑아 만들어야 하는 K의 값
# cnt = K의 값이 된 개수

T = int(input())
A = list(range(1,13)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = len(A)
    cnt = 0
    for i in range(1, 1 << arr): # 1부터 하는 이유는 공집합은 검사할 필요 없어서서
       result = 0
       if str(bin(i)[2:]).count('1') == N:
            for j in range(arr):
                if i & (1 << j):
                    result += j + 1
       if result == K:
           cnt += 1
    print(f'#{tc} {cnt}')