import sys
sys.stdin = open('input (3).txt')
T = int(input())
for tc in range(1,T+1):
    s = list(input())
    # 체크할 리스트 초기화
    ch_li = []
    for i in range(len(s)):
        # i 번째 인덱스 값을 ch_li 에 넣기
        ch_li.append(s[i])
        # 현재 길이를 ln 에 담기
        ln = len(ch_li)
        # 현재 ch_li의 값과 입력 받은 s의 i번째 인덱스 이후의 값부터 같은 길이의 다음 문자까지 비교
        # ex) KOREAKOREAKOREAKOREAKOREAKOREA 의 경우
        # i가 3 이면  ch_li = ['K', 'O', 'R'] , ln = 3
        # 그러면 s[3:6] -> ['E', 'A', 'K'] 와 서로 비교후 맞으면 중지
        if ch_li == s[ln:ln+ln]:
            break
    result = len(ch_li)
    print(f'#{tc} {result}')
