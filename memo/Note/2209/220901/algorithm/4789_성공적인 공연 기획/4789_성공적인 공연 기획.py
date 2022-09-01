T = int(input())
for tc in range(1,T+1):
    s = input()
    cnt = 0
    result = 0
    for i in range(len(s)):
        if s[i] != '0':
            if cnt >= i:
                cnt += int(s[i])
            else:
                result += i - cnt
                cnt = i + int(s[i])
    print(f'#{tc} {result}')

# ?? 자세히 보기로...