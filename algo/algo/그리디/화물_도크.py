# 시작 시간을 기준으로 화물차 작업시간과 종료 시간 배열을 오름차순 정렬
# 그리고 시작과 종료 사이에 신청한 화물차가 있을 수 있기에 
# 브루트 포스로 모든 idx 위치에서 새롭게 조사하기

for tc in range(1, int(input())+1):
    n = int(input())
    form = [list(map(int,input().split())) for _ in range(n)]
    form.sort(key=lambda x:(x[0], x[1]), reverse=True)
    result = 0
    for x in range(n):
        s,e = form[x]
        check = 1 
        for i in range(x+1, n):
            now_s, now_e = form[i]
            if s >= now_e: s, check = now_s, check+1
        if check > result: result = check
    print('#%d'%tc, end=' ')
    print(result)