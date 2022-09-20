li = list(input()) # 01D06079861D79F99F
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
        num_six = num +  num_six
        six_bit.append(num_six)

# 24개
# 0000 1111 1001 0111 1010 0011
six = ''.join(six_bit)
six = list(map(int,str(six)))

# print(six) # [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]

while True:
    ch = []
    x = cnt = sum = 0
    # print(six)
    if len(six) >= 7:
        ch = six[cnt*7:(cnt+1)*7]
        # print(ch)
        for j in range(len(ch)-1,-1,-1):
            # print(ch[j])
            sum += ch[j]*(2**x)
            x += 1
        print(sum)
        cnt += 1
        six = six[cnt*7:]

    else:
        ch = six[cnt*7:]
        for j in range(len(ch)-1,-1,-1):
            sum += ch[j]*(2**x)
            x += 1
        print(sum)
        break


# r = len(byte)//7
# for i in range(r):
#     sum = 0
#     x = 0
#     ch = byte[i*7:(i+1)*7]
#     for j in range(len(ch)-1,-1,-1):
#         sum += ch[j]*(2**x)
#         x +=1
#     print(sum)
