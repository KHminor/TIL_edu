import sys
sys.stdin = open('input.txt')

'''
3
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
7 7 19 1 -18 5 -9 -11 19 18
'''

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split())) # 입력 값을 리스트로 담기
    # [19, 6, 16, 19, 15, 16, 8, 13, 16, 10]
    N = len(arr)  # arr의 개수

    for i in range(1, 1<<N):  # i=1
        # 원소가 N개일 경우의 모든 부분집합의 수를 구하기 위해서는 1<<N을 사용해야 한다.
        # 또는 2**N
        # 모든 경우의 수 구할건데
        # 각 경우의 수로 만들어지는 부분집합들의
        # 합이 0이 되는 순간이 있는지 확인할 것
        result = 0

        # 내가 가진 각 요소들을 부분집합에
        for j in range(N):  # j=0
            # 포함 시킬거냐 말거냐를 판단해야한다.
            # i == i 번째 경우의 수
            # j == arr[j] 번째 요소를 넣을거냐 말거냐
            if i & (1<<j): # i 에 대한 j번째 비트가 1인지 확인
                print(f'{i}번째 경우의 수 {bin(i)[2:]:0>4}')
                print(f'{j}번째 요소 비교 {bin(1 << j)[2:]:0>4}')
                result += arr[j]
                # print(result)
        if result == 0:
            print(f'#{tc} {1}')
            break
    else:
        print(f'#{tc} {0}')