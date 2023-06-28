from collections import deque

# dfs 방식으로 푼 코드
# bfs로 풀어보니 시간이 더 오래 걸렸다.
def solution(numbers, target):
    answer = 0
    stack = [[0,0]] # 시작 stack
    while stack:
        idx, hap = stack.pop()
        if idx < len(numbers):
            stack.append([idx+1, hap+numbers[idx]])
            stack.append([idx+1, hap-numbers[idx]])
        else:
            if hap == target:
                answer += 1
    return answer


# bfs 방식으로 푼 코드
def solution(numbers, target):
    answer = 0
    que = deque([[0,0]]) # 시작 queue
    while que:
        idx, hap = que.popleft()
        if idx < len(numbers):
            que.append([idx+1, hap+numbers[idx]])
            que.append([idx+1, hap-numbers[idx]])
        else:
            if hap == target:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))