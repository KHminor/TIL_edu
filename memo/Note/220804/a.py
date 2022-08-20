import sys
sys.stdin = open('a.txt')



def bubble(li,cnt):
    n = cnt-1
    print(li)
    while n != 0 :
        for i in range(cnt-1):
            if li[i] > li[i+1]:
                li[i], li[i + 1] = li[i+1], li[i]
        n -= 1
    return  li


T = 10  # 테스트 케이스
for tc in range(1, T+1):
    dum = int(input())     # 덤프 가능 횟수   ex) 2

    flatten_li = list(map(int,input().split()))
    cnt = minus = 0         # 최고점과 최저점의 차이의 값 minus 와 cnt 값 초기화
    for c in flatten_li:
        cnt += 1
    print(cnt)
    li = bubble(flatten_li, cnt)
print(li)