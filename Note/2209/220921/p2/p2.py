# 6자리 숫자에 대해서 완전 검색을 적용해서 Baby-gin을 검사해보시오.
# input
# 4
# 124783
# 667767
# 054060
# 101123

# 우선 순열을 구하자.
# 첫번째 방식 (역순으로 변경)

def Baby_gin(i,k):
    global result
    if i == k:
        li = [0]*10
        cnt = 0
        for x in range(6):
            li[num[x]] +=1
            if li[num[x]] == 3:
                li[num[x]] -= 3
                cnt += 1
        for y in range(len(li)-2):
            if li[y] >=1 and li[y+1] >=1 and li[y+2] >= 1:
                li[y] -= 1
                li[y+1] -=1
                li[y+2] -=1
                cnt += 1
        if cnt == 2:
            result = 'True'

    else:
        for j in range(i,k):
            num[i],num[j] = num[j],num[i]
            Baby_gin(i+1,k)
            num[i], num[j] = num[j], num[i]



T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input()))
    result = ''
    Baby_gin(0,6)
    if result == '':
        print('False')
    else:
        print(result)
# 124783