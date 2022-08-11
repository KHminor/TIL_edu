import sys
sys.stdin  = open('input.txt')

N = int(input())
arr = list(map(int,input().split()))

# 최대값의 위치, 같은 값이 있을때는 맨 오른쪽 인덱스 넣기
# maxidx = 0
# for i in range(1,N):
#     if arr[i] >= arr[maxidx]:
#         maxidx = i
#
# print(maxidx)

# ============================================================

# # 버블 정렬
# for i in range(N-1,0,-1): # 구간의 맨 끝 인덱스
#     for j in range(i): # 인접 원소 중 왼쪽 원소 인덱스
#         if arr[j] > arr[j+1]: # 오름차순, 더 큰수를 오른쪽으로
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# =============================================================

# 카운트 정렬
tmp = [0] * N
c = [0] * 101  # 0부터 100 까지의 개수, 인덱스가 100까지 있어야 함
for i in range(N):
    c[arr[i]] += 1

for j in range(1,101):  # 개수 누적
    c[j] += c[j-1]

for k in range(N-1, -1, -1): # 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
    