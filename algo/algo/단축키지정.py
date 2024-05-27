import sys
input = sys.stdin.readline
_set = set()
for _ in range(int(input())):
    s = list(input().rstrip('\n').split(' '))
    flag = False
    for i in range(len(s)):
        if s[i][0].lower() not in _set:
            _set.add(s[i][0].lower())
            s[i] = '[%s]'%s[i][0]+s[i][1:]
            flag = True
            break
    if not flag:
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j].lower() not in _set:
                    _set.add(s[i][j].lower())
                    s[i] = s[i][:j]+'[%s]'%s[i][j]+s[i][j+1:]
                    flag = True
                    break
            if flag: break
    print(*s)