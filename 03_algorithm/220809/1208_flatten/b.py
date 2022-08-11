import sys
sys.stdin = open('a.txt')


T = 10  # 테스트 케이스
for i in range(2):
    dump = int(input())     # 덤프 가능 횟수   ex) 2

    f_li = list(map(int,input().split()))
    cnt = minus = 0         # 최고점과 최저점의 차이의 값 minus 와 cnt 값 초기화
    for c in f_li:
        cnt += 1

    n = cnt - 1
    while n != 0:
        for i in range(cnt - 1):
            if f_li[i] > f_li[i + 1]:
                f_li[i], f_li[i + 1] = f_li[i + 1], f_li[i]
        n -= 1

    min = f_li[0]  # 1
    max = f_li[-1]  # 100
    print(f_li)

    r_dump = point = 0

    while r_dump != dump:
        point = 0
        print(f_li)

        for i in range(cnt):
            if f_li[i] <= min:
                f_li[i] += 1
                r_dump += 1
                point +=1
            else:
                min = f_li[i]
                break

        for j in range(cnt-1,0,-1):
            if f_li[j] >= max:
                f_li[j] -= 1
                point -= 1
                if point <= 0:
                    r_dump = dump
                    break
print(f_li)

