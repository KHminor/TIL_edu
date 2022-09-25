# 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
# 마치는 시간을 오름차순 정렬한 후
# 현재 회의가 마치는 시간보다 다음 회의의 시작 시간이 이르다면 안되며
# 후의 시간일 경우에만 회의를 시작할 수 있다.

# 시작 시간을 리스트의 인덱스를 활용하여 값을 넣어주자.

N = int(input())
line = [[] for _ in range(15)]
e_t = []

for _ in range(N):
  s,e = map(int,input().split())
  line[e].append(s)
  e_t.append(e)
e_t.sort()
print(line)
print(e_t)
print('='*30)
while e_t:
    e = e_t.pop(0)
    for i in e_t:
        print('i의 값: ',i)
        for j in range(len(line[i])):
            if line[i][j] >= e:
                break
            else:
                a = line[i].pop(j)
                print(a,': a의 값')
        if line[i][j] >= e:
            break
        print(line)
        print(e_t)
    print('=='*10)