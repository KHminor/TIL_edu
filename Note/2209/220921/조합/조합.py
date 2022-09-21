# 반복문을 사용한 조합
# N = 10
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             print(i,j,k)
#

# 재귀를 사용한 조합
def nCr(n,r,s): # n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)
            
A = [1,2,3,4,5]
n = len(A)
r = 3
comb = [0]*r
nCr(n,r,0)

# 재귀 조합
