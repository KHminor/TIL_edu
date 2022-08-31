import sys
sys.stdin = open('input (3).txt')
T = int(input())
for tc in range(1,T+1):
    s = list(input())
    # print(s)
    ch_li = []
    for i in range(len(s)):
        ch_li.append(s[i])
        ln = len(ch_li)
        if ch_li == s[ln:ln+ln]:
            break
    result = len(ch_li)
    print(f'#{tc} {result}')

# 0, ln
# 0~4, 5~9