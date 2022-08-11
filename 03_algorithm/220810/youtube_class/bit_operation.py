arr = ['Fish', 'And', 'Chips']
N = len(arr)

for i in range(1<<N):
    for j in range(N) :
        if i & (1<<j):
            print(f'{i}번째 경우의 수 {bin(i)[2:]}')
            print(f'{j}번째 요소 비교 이진수 값 {bin(1<<j)[2:]})
            print(arr[j],end='')
    print()