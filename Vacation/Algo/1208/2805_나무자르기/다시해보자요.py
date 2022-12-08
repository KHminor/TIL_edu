# 이분 탐색: 리스트 전체를 방문해서 셈을 해야할 경우 시간초과가 뜨면 적용해보자
# 결국 이분법으로 결과를 도출할 때는 해당 결과를 얻었을때를 찾는것이 아니라
# 시작지점과 마치는 지점이 교차될 때 해당 포인트의 마치는 지점을 출력하는 것이 답이 된다.

import sys
n,m = map(int,sys.stdin.readline().split())
li = sorted(list(map(int,sys.stdin.readline().split())))
li.reverse()

sm = 1
bg = li[0]

while bg >= sm:
    cnt = 0
    mid = (sm+bg) // 2

    for i in li:
        if i >= mid:
            cnt += i - mid

    if cnt >= m:
        sm = mid + 1
    else:
        bg = mid - 1


print(bg)