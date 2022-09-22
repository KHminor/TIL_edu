import sys
sys.stdin = open('sample_input (7).txt')
T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    one = [0]*10
    two = [0]*10
    f = 'True'
    result = 0
    for i in range(len(arr)):
        if i % 2:
            two[arr[i]] += 1
            if two[arr[i]] == 3:
                result = 2
                f = 'False'
                break
        else:
            one[arr[i]] += 1
            if one[arr[i]] == 3:
                result = 1
                f = 'False'
                break

        for j in range(8):
            if two[j] >= 1 and two[j+1] >= 1 and two[j+2] >= 1:
                result = 2
                f = 'False'
                break

            elif one[j] >= 1 and one[j+1] >= 1 and one[j+2] >= 1:
                result = 1
                f = 'False'
                break
        if f == 'False':
            break

    print(f'#{tc} {result}')