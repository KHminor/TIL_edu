import sys
sys.stdin = open('input.txt')

tc = int(input()) # 테스트 케이스 수

for i in range(tc):
    t_num = num = int(input()) # 입력 값 받기

    cnt_li = [0]*10 # 0부터 9까지 총 10개의 숫자의 카운트를 담을 리스트
    run = tri = 0 # run과 triplet을 0으로 초기화
    # 아래의 코드는 num의 값을 10으로 나눈 나머지 값에 해당하는 인덱스의 값을 1증가시켜
    # cnt_li 에 카운트를 해주는 작업
    while num > 0:
        cnt_li[num%10] += 1
        num = num//10

    # 아래의 코드는 카운트 되어있는 cnt_li의 값에서 triplet 을 우선 찾아주는 작업
    for j in range(0,len(cnt_li)-2):
        while cnt_li[j] > 2 :
            if cnt_li[j] >= 3:
                tri += 1
                cnt_li[j] -= 3

    # 아래의 코드는 3개의 값이 연속되는 run 을 찾아주는 작업
        while cnt_li[j] >= 1:
            if cnt_li[j+1] >= 1 and cnt_li[j+2] >= 1:
                run += 1
                cnt_li[j] -= 1
                cnt_li[j+1] -= 1
                cnt_li[j+2] -= 1
            else:
                break

    # 위에서 작업한 tri와 run을 합한 값이 2의 경우 baby-gin임을 출력해주는 코드
    if run+tri == 2:
        print(f'This number {t_num} is baby-gin')
    else:
        print(f'{t_num} byebye')