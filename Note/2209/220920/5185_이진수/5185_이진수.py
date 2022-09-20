import sys
sys.stdin = open('sample_input (2).txt')
T = int(input())
for tc in range(1,T+1):
    N, li = input().split()
    li = list(li) # 01D06079861D79F99F
    dic = {
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111',
    }

    s_ch = ['A','B','C','D','E','F']

    six_bit = []
    for i in range(len(li)):
        num_six = ''
        if li[i] in s_ch:
            six_bit.append(dic.get(li[i]))
        else:
            num = li[i]
            for _ in range(3):

                num_six = str(int(num)%2) + num_six
                num = str(int(num)//2)
            num_six = num + num_six
            six_bit.append(num_six)

    six = ''.join(six_bit)
    print(f'#{tc} {six}')