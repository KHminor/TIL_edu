
cnt = 0

def solution(word):
    li = ['']*5
    
    def find(idx): 
        global cnt   
        if "".join(li) == word: return cnt
        elif idx == 5: return
        else:
            for i in ['A','E','I','O','U']:
                cnt += 1
                li[idx] = i
                if find(idx+1): return cnt
                li[idx] = ''
    return find(0)

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))