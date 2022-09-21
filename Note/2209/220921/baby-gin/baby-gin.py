# 아래는 N에서 R개 만큼만 고르는 경우
def f(i,k,r):
    if i == r:
        print(p)
    else:
        for j in range(k):      # uesd 는 처음부터 끝까지 가는 것니까
            if used[j] == 0 :   # a[j] 가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 가 사용됨으로 표시
                p[i] = a[j]     # p[i] 는 a[j] 로 결정
                f(i+1, k,r)       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 6
R = 6
a = [1,2,4,7,8,3]
used = [0]*N
p = [0]*R
f(0,N,R)

