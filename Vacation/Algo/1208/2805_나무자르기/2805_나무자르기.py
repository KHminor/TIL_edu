import sys
# n: 나무의 수
# m: 가져가려는 나무의 길이

def cut(cnt):
    if li[0] != li[1]:
        while li[0] > li[1]:
            cnt += 1
            li[0] -=1
            result = li[0]
            if cnt == m:
                return result

        while cnt != m:
            for i in range(1,len(li)):
                if li[i]== li[i-1]:
                    cnt +=1
                    li[i-1] -=1
                    result = li[i-1]
                    if cnt == m:
                        return result
                    cnt +=1
                    li[i] -=1
                    if cnt == m:
                        return result
                    break
                else:
                    break

        return result
    else:
        while cnt != m:
            for i in range(1, len(li)):
                if li[i] == li[i - 1]:
                    cnt += 1
                    li[i-1] -= 1
                    result = li[i-1]
                    if cnt == m:
                        return result
                    cnt += 1
                    li[i] -= 1
                    if cnt == m:
                        return result
                    break
                else:
                    break
        return result



n,m = map(int,sys.stdin.readline().split())
li = sorted(list(map(int,sys.stdin.readline().split())))
li.reverse()
print(li)

cnt = 0

print(cut(cnt))