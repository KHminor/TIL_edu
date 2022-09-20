# N = 0.625
# 0.101 (이진수)
# = 1*2-1 + 0*2-2 + 1*2-3
# = 0.5 + 0 + 0.125
# = 0.625

N = int(float(input())*1000)
result = []
cnt = 3
# print(N)
while cnt:
    N = N*2
    moc = str(N//1000)
    N = N-1000
    print(N)
    if N < 0:
        result.append('0')
        N = 1000-N
    else:
        result.append(moc)
    cnt -= 1
    print(result)
a = len(result)
# print(a)
N = int(''.join(result))
print(N)
# print(N*(10**-a))
# print(5*10**-a)