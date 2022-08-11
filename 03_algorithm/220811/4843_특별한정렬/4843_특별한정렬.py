import sys
sys.stdin = open('sample_input.txt')
# 테스트 케이스의 수
T = int(input())

for tc in range(1,T+1):
    # 입력 받을 정수의 개수
    N = int(input())
    arr = list(map(int,input().split())) # 리스트로 받기

    for a in range(N-1, 0, -1):  # 버블 정렬을 이용하여 오름차순 정렬 시키기
        for b in range(N-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]

    li = []  # 가장 큰 수 , 가장 작은 수식으로 번갈아 가며 값을 넣을 li 초기화
    M = 6  # 10개만 출력을 하길 원하기에 1,6까지 하여 5번 반복하기 위한 값

    for i in range(1,M): # 반복문을 통해서 인덱스 값을 활용하여
            li.append(arr[(N-1)-(i-1)]) # 해당 배열에서 가장 큰 인덱스 값에서 한칸씩 안으로 접근하여 append 하기
            li.append(arr[i-1]) # 해당 배열에서 가장 작은 인덱스 값에서 한칸씩 밖으로 접근하여 append 하기

    print(f'#{tc}', end=' ')
    print(*li)



