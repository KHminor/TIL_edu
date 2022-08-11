# N개의 정수가 들어있는 배열
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오

# N = 숫자의 개수
# M = 묶음
# 오름차순 정렬을 한 뒤 앞에서부터 혹은 뒤에서부터 더한 후 차이 구하기
import sys
sys.stdin = open('sample_input.txt')
T = int(input()) # 테스트 케이스
for ct in range(1,T+1):
    N, M = map(int,input().split())

    num_li = list(map(int, input().split()))
    r = N-M+1  # 범위
    sum_num_li = [0]*r  # 지정한 영역만큼 더해줄 빈 list 생성

    for sum in range(r):  # 지정한 영역만큼 그룹핑 할 수 있는 수만큼 반복하기.
        for j in range(sum,sum+M): # num_list[sum] 값을 기준으로 지정한 영역 개수만큼 더하기
            sum_num_li[sum] += num_li[j]


    while r != 0:
        for z in range(r-1):
            if sum_num_li[z] > sum_num_li[z+1]:
                sum_num_li[z] , sum_num_li[z + 1] = sum_num_li[z+1] , sum_num_li[z]
        r -= 1

    result = sum_num_li[-1] - sum_num_li[0]  # 범위의 가장 큰 값과 가장 작은 값의 차
    print(f'#{ct} {result}')
