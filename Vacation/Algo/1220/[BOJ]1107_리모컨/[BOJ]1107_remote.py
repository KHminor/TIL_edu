import sys

n = input()
m = int(input())
result1 = result2 = 0
li = [1]*10
if not m: print(len(n))
else:
    for i in map(int,sys.stdin.readline().split()):
        li[i] = 0

    final = ''
    cnt = 0
    for i in n:
        j = int(i)
        cnt += 1
        if li[j]:
            final += i
        else:
            bCnt = sCnt = 0
            b = s = j
            # i 가 9 이전까지 체크
            while b < 10:
                if li[b]:
                    break
                elif b == 9 and not li[b]:
                    bCnt = 10
                    break
                b += 1
                bCnt += 1
            while s > -1:
                if li[s]:
                    break
                elif s == 0 and not li[s]:
                    sCnt = 10
                    break
                s -= 1
                sCnt += 1

            # 최소한을 구하기에 반대로 대입
            if bCnt > sCnt:
                final += str(s)
            else:
                final += str(b)


    if abs(int(n)-100) > cnt:
        result1 = cnt+abs(int(final)-int(n))
    else:
        result1 = abs(int(n)-100)


    # 지금 가지고 있는 숫자로 만들 수 있는 한단계 작은 값과 한단계 큰 값을 구해야 함

    bigInt = samllInt = ''
    for i in n:

        if li[int(i)]:
            bigInt += i
            samllInt += i
        else:
            j = int(i)
            b = s = j
            while b < 10:
                if li[b]:
                    bigInt += str(b)
                    break
                elif b == 9 and not li[b]:
                    b = 99
                    break
                b += 1

            while s > -1:
                if li[s]:
                    samllInt += str(s)
                    break
                elif s == 0 and not li[s]:
                    s = 99
                    break
                s -= 1

            if b == 99 and s != 99:
                bigInt += str(s)
            elif s == 99 and b != 99:
                samllInt += str(b)

    bigInt, samllInt = int(bigInt), int(samllInt)


    if abs(int(n)-bigInt) > abs(int(n)-samllInt):
        result2 = len(n)+samllInt-int(n)
    else:
        result2 = len(n)+bigInt-int(n)

    # print(result1,result2)
    if result1 > result2:
        print(result2)
        # print(1)
    else:
        print(result1)
        # print(2)
