import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    s = ''
    for i in range(15):         # 단어의 길이가 15 이하라고 해서
        for j in range(5):
            if len(arr[j]) <= i:# 해당 배열의 길이가 i보다 클 경우만 조사
                continue
            s += arr[j][i]
    print(f'#{tc} {s}')
