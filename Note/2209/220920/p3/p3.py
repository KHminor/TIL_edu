li = list(input()) # 01D06079861D79F99F
dic = {
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

pass_dic = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}
pas_ch = ['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111' ]
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

six = ''.join(six_bit)
six = list(six)
ch = []
x = 0
while len(six) >= 6:
    cnt = 0
    # print(six)
    ch = six[:cnt+1*6]
    ch = ''.join(ch)
    if ch in pas_ch:
        print(pass_dic.get(ch))
        cnt += 1
        x = 0
    else:
        x = 1
    six = six[cnt*6+x:]

# 0269FAC9A0


