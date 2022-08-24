import sys
sys.stdin = open('input.txt')
N = 9                                               # 주어지는 숫자는 총 9개
dic = {}                                            # 기존 인덱스 값을 저장하기 위해 dict 초기화
cnt = 0                                             # 출력값을 위해 cnt 초기화
arr = []                                            # 오름차순으로 정렬하기 위해 list 초기화
for _ in range(N):
    num = int(input())
    arr.append(num)                                 # 입력받은 num의 값을 arr에 추가
    cnt += 1                                        # num의 입력 받은 순서를 1~9까지이기에 +1 
    dic[num] = cnt                                  # 현재 num의 값을 key, 원래 인덱스 값 cnt를 value로 지정
ln = len(arr)
for i in range(ln-1, 0, -1):                        # 버블 정렬
    for j in range(ln-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j + 1] = arr[j+1], arr[j]
max = arr[-1]                                       # 가장 큰 값을 max에 지정
print(max)
print(dic[max])

