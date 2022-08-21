import sys
sys.stdin = open('input.txt')
T = int(input())                                        # 테스트 케이스 수

for tc in range(1,T+1):
    N = int(input())                                    # 사각형 크기
    arr = [list(map(int, input())) for _ in range(N)]   # 배열 형식으로 값 받아오기
    ch = sum = r = 0                                    # 변수 초기화
    t = 1                                               # moc과 함께 이용하기 위해 우선 값 저장
    moc = N // 2                                        # moc의 값을 기준으로 데칼코마니처럼 되어서 값 저장
    for i in range(N):
        j = moc - ch                                    # j의 값을 보기 쉽게 따로 저장
        for _ in range(t):                              # 각 줄마다 입력받는 값이 달라지기에 t 만큼 반복
            sum += arr[i][j]
            j += 1                                      # 반복문이 남아있을 경우 1씩 값을 증가
        if r >= moc:                                    # 현재 라운드가 moc의 값보다 클 경우
            ch -= 1
            t -= 2
        else:                                           # 현재 라운드가 moc의 값보다 작을 경우
            ch += 1
            t +=2
        r += 1                                          # 라운드 1씩 증가
    print(f'#{tc} {sum}')