def selection_sort(arr, N):
    for i in range(N):
        min_idx = i # 가장 첫번째 값을 기준으로 끝까지 순회하는 것을 하기 위해
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                # 인덱스 값으로 해당 인덱스가 가장 작다는 것을 저장
                min_idx = j
        arr[i] , arr[min_idx] = arr[min_idx], arr[i]



arr [93, 3, 61, 52, 81, 6, 91]
N = len(arr)
li = selection_sort(arr, N)