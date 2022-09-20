import sys
sys.stdin = open('input.txt')
byte = input()
byte = byte.replace(' ', '')
byte = list(map(int,byte))

r = len(byte)//7
for i in range(r):
    sum = 0
    x = 0
    ch = byte[i*7:(i+1)*7]
    for j in range(len(ch)-1,-1,-1):
        sum += ch[j]*(2**x)
        x +=1
    print(sum)
