import sys
sys.stdin = open('GNS_test_input.txt')
T = int(input())
for _ in range(T):
    tc, ln = input().split()
    ln = int(ln)
    li = list(input().split())

    # 딕셔너리로 해당 값에 대한 카운팅 하기
    dic = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0}

    for i in li:
        dic[i] += 1

    s = ''
    s += dic.get("ZRO") *("ZRO" + ' ') + dic.get("ONE") *("ONE" + ' ') + dic.get("TWO") *("TWO" + ' ') + \
    dic.get("THR") *("THR" + ' ') + dic.get("FOR") *("FOR" + ' ') + dic.get("FIV") *("FIV" + ' ') + dic.get("SIX") *("SIX" + ' ') + dic.get("SVN") *("SVN" + ' ') +\
    dic.get("EGT") *("EGT" + ' ') + dic.get("NIN") *("NIN" + ' ')
    print(f'{tc} {s}')

