def solution(num, total):
    answer = []
    moc = total//num
    if total%num:
        for i in range(num//2):
            answer.append(moc-i)
            answer.append(moc+i+1)
    else:
        for i in range(num//2+1):
            answer.append(moc-i)
            if i != 0: answer.append(moc+i)
            
    return sorted(answer)

print(solution(3,12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))