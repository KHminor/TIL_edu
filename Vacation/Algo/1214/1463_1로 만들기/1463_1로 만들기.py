# 해당 문제에서 DP를 사용하는 이유?
# 우선 그리디하게 문제를 풀게 되면 틀릴 수 밖에 없는 이유는: 어떤 연산을 해야 가장 빠르게 처리될 수 있는지 모르기 때문
# 그래서 해당 숫자에 대해 모든 연산을 한 이후 해당 하는 값이 1이 됐을 경우의 최소 연산은 담아놓은 후
# 또다시 해당 숫자가 나올 경우 반복하여 수행하지 않고 저장되어 있는 값에서 + 추가 연산을 해주면 되기 때문에
# DP를 사용하는 것 같다.
# 중요한것: 해당 숫자를 해당 연산으로 했을때 무조건적으로 최선이다라고 할 수 없다라는 것. (DP를 사용해서 모두 해봐야한다)

def find(n,cnt):
    if n == 1:
        if ch_dic[x] > cnt:
            ch_dic[x] = cnt
        return cnt
    elif ch_dic[n] != 1000001:
        return ch_dic[n]+cnt
    else:
        if n%3 == 0:
            check = find(n//3,cnt+1)
            if x !=n and ch_dic[n] > cnt:
                ch_dic[n] = cnt
            if x ==n and ch_dic[n] > check:
                check
            # return
        if n%2 == 0:
            check = find(n//2,cnt+1)
            if x !=n and ch_dic[n] > cnt:
                ch_dic[n] = cnt
            if x ==n and ch_dic[n] > check:
                check
            # return
        if n-1 >= 1:
            check = find(n-1,cnt+1)
            if x !=n and ch_dic[n] > cnt:
                ch_dic[n] = cnt
            if x ==n and ch_dic[n] > check:
                check

x = int(input())

cnt = 0
ch_dic = {x:1000001 for x in range(x+1)}
ch_dic[0] = 0
ch_dic[1] = 0
ch_dic[2] = 1
ch_dic[3] = 1
find(x,cnt)
print(ch_dic[x])