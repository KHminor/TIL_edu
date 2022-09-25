import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())

    n_w = list(map(int,input().split()))
    m_w = list(map(int,input().split()))

    n_w.sort(reverse=True)
    m_w.sort(reverse=True)

    sum = 0
    for i in m_w:
        for j in range(len(n_w)):
            if i >= n_w[j]:
                sum += n_w[j]
                n_w.pop(j)
                break

    print(f'#{tc} {sum}')