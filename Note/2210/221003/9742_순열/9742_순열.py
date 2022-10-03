# 순열 문제를 풀때 sort 없이 순서대로 나오게 하려면
# 아래와 같은 방식보다는 visited를 사용해야한다.

# def nPr(s,n):
#     if s == n:
#         ch_li.append(num_li[:])
#     else:
#         for i in range(s,n):
#             num_li[s],num_li[i] = num_li[i],num_li[s]
#             nPr(s+1,n)
#             num_li[s], num_li[i] = num_li[i], num_li[s]

import sys

def nPr(s,n):
    global num
    if ch_li:
        return
    if s == n:
        if num == ch_num:
            ch_li.append(li[:])
            return

        num += 1
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                li[s] = num_li[i]
                nPr(s+1,n)
                visited[i] = 0

while 1:            # while 문을 넣은 것은 input 값이 없을 때까지 받기위해
    data = sys.stdin.readline().rstrip().split()
    if len(data) != 2:
        break
    a, b = data
    num_li, ch_num = list(a),int(b)
    n = len(num_li)
    num = 1
    ch_li = []
    visited = [0]*n
    li = [0]*n
    nPr(0,n)

    s = ''
    if num == ch_num:
        for i in ch_li[0]:
            s += i
        print(f'{a} {b} = {s}')
    else:
        print(f'{a} {b} = No permutation')