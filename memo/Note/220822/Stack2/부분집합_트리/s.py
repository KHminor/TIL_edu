def f(i,N):         # 부분 집합
    if i == N:
        print(bit)
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i + 1, N)

bit = [0]*5
f(0,5)