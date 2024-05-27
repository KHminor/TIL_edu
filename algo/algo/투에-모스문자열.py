k = int(input())
cnt = 0
result = '0'
if k == 0: print(1)
else:
    while True:
        cnt += 1
        tmp = ''
        for i in result:
            if i == '0': tmp += '1'
            else: tmp += '0'
        result += tmp
        if len(result) >= k//2: # 홀수를 대비해서
            idx = k//2-1
            if result[idx] == '0': print(1)
            else: print('0')
            break

def tue(n):
    if n == 0: return 0
    elif n%2: return 1-tue(n//2)
    else: return tue(n//2)

print(tue(int(input())-1))


