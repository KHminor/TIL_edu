# 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다
# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
# 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
def digital(i,n):
    global min_sum, s
    if i == n:
        print(num)
        # [2,3,1,0]
        for x in range(len(num)):
            if not arr[x][num[x]]:
                s = 0
                break
            s += arr[x][num[x]]

        if 0 < s < min_sum:
            min_sum = s
            s = 0
            # if s >= min_sum:
            #     break
        else:
            s = 0


        print(min_sum)
        print('===============')
    else:
        for j in range(i,n):
            num[i],num[j] = num[j],num[i]
            digital(i+1,n)
            num[i], num[j] = num[j], num[i]

min_sum = 100000
s = 0
T = int(input())
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
num = [i for i in range(N)]
# print(num)
digital(0,N)