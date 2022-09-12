def f(i, N):
    global sewr
    if i == N:      # i가 출력할 횟수랑 같아진다면 중단.
        s = 0               # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == 10:
            sewr += 1   # 부분집합의 합이 10인 경우의 수
    else:
        bit[i] = 1  # A[i]가 부분 집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N )
sewr = 0
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*5
f(0,5)

print(sewr)