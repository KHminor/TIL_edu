import sys
sys.stdin = open('sample_input (1).txt')

def merge(arr):
    # 더 이상 쪼갤 수 없는 상황이 올때까지 쪼갠다.
    if len(arr) ==1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]    # 왼쪽 절반
    right = arr[mid:]   # 오른쪽 절반

    print(left,right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    print(nums)

    # 병합 과정에서 왼쪽 끝이 오른쪽 끝보다 큰 경우의 수
    result = 0
    # 병합 정렬을 끝낸 리스트
    ans = merge(nums)
    print(f'#{tc} {ans} {result}')