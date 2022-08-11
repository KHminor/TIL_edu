# 평탄화 수행 후 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
# 제한된 횟수 만큼 옮겼을 때 최고점과 최저점의 차이를 반환하는 프로그램
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

    min = f_li[0]
    max = f_li[-1]

    r_dump = point = 0
    while r_dump != dump:
        point = 0
        print(f_li)

        for i in range(cnt):
            if f_li[i] == min:
                f_li[i] += 1
                r_dump += 1
                point +=1
                if r_dump == dump:
                    break
            else:
                min = f_li[0]
                break
        print(f'현재 포인트 {point}')
        for j in range(cnt-1, -1, -1):
            if f_li[j] == max:
                f_li[j] -= 1
                point -= 1
                if point == 0:
                    max = f_li[-1]
                    break
                if f_li[j-1] < f_li[j] :
                    f_li[j] -= f_li[j] - f_li[j-1]
                    point -= f_li[j] - f_li[j-1]
                    if point == 0:
                        max = f_li[-1]
                        break


            else:
                max = f_li[-1]
                if point == 0:
                    break

        if r_dump == dump:
            min = f_li[i+1]
        if 0 <= max - min <= 1:
            break


    print(max- min)