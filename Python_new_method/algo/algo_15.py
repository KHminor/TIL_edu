def solution(arr, divisor):
    li = [i for i in arr if i%divisor == 0]
    return sorted(li) if len(li) else [-1]


def solution(arr, divisor): return sorted([i for i in arr if i%divisor == 0]) or [-1]


solution([5, 9, 7, 10], 5)