# N이 32850일 경우,
# 50,000 원 : 0개     0
# 10,000 원 : 3개     1
# 5,000 원 : 0개      2
# 1,000 원 : 2개      3
# 500 원 : 1개        4
# 100 원 : 3개        5
# 50 원 : 1개         6
# 10 원 : 0개         7
import sys
sys.stdin = open('input.txt')
T = int(input())
c_li = [50000, 10000, 5000, 1000, 500, 100, 50, 10]         # 요금에 대한 리스트
for tc in range(1, T+1):
    cost = int(input())                                     # 요금
    dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}          # 요금 별 카운팅을 위한 dict 초기화
    for i in range(len(c_li)):                              # 모든 요금을 한번 씩 돌아가도록 반복
        if cost >= c_li[i]:                                 # 비용이 해당 요금보다 크거나 같을 경우
            dic[i] = cost//c_li[i]                          # i에 해당하는 잔돈으로 요금을 나눈 몫의 수만큼 카운팅
            cost = cost%c_li[i]                             # 차감한 나머지 돈을 다시 초기화
    print(f'#{tc}')
    print(*list(dic.values()))