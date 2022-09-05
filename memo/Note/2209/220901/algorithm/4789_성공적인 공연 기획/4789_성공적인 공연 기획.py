T = int(input())
for tc in range(1,T+1):
    s = input()
    # 1 이 총 몇개였는지 체크하는 변수
    cnt = 0
    # 고용해야하는 인원 체크하는 변수
    result = 0
    for i in range(len(s)):
        # 해당 인덱스 값이 0 이 아닌 경우
        if s[i] != '0':
            # 현재 cnt 값과 i의 값이 같거나 cnt가 클 경우
            if cnt >= i:
                # 현재 cnt에 s의 i 번째 인덱스 값을 int화 하여 더해주기
                cnt += int(s[i])
            else:
                # 지금까지 0이 몇개 있었는지 확인 후 result 에 더해주기
                result += i - cnt
                # 고용했다 생각하고 cnt 채워주기
                cnt = i + int(s[i])
    print(f'#{tc} {result}')

