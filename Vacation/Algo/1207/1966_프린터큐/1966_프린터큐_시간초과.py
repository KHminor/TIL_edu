import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    # n: 문서의 개수,
    # m: 현재 Q에서 몇 번째에 놓여져 있는지(0이 가장 왼쪽)
    n, m = map(int,sys.stdin.readline().split())
    # 입력받은 순서 리스트
    li = deque(list(map(int,sys.stdin.readline().split())))
    # li =

    # li에서 중복을 제거한 오름차순 정렬한 요소들
    st_li = sorted(list(set(li)))
    # 현재 출력해야할 가장 큰 값
    st_li_mx = max(st_li)

    # 출력된 횟수?? li에서 빠져나간 횟수??
    cnt= 0

    while True:
        if li[0] == st_li_mx and m == 0:
            cnt += 1
            break
        elif li[0] == st_li_mx:
            li.popleft()
            m -= 1
            if len(st_li) != 1:
                st_li.pop()
                st_li_mx = st_li[-1]
            cnt += 1
        else:
            if m != 0:
                m -= 1
            else:
                m = len(li)-1
            li.append(li.popleft())


    print(cnt)