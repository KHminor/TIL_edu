def pre_order(n):
    if not n == None:
        li.append(n)
        if n in ch1 or n in ch2:
            pre_order(ch1.get(n))
            pre_order(ch2.get(n))
    result = ''.join(li)
    return result

def in_order(n):
    if not n == None:
        if n in ch1 or n in ch2:
            in_order(ch1.get(n))
            li.append(n)
            in_order(ch2.get(n))
        else:
            li.append(n)
    result = ''.join(li)
    return result

def post_order(n):
    if not n == None:
        if n in ch1 or n in ch2:
            post_order(ch1.get(n))
            post_order(ch2.get(n))
            li.append(n)
        else:
            li.append(n)
    result = ''.join(li)
    return result

# 노드의 개수
N = int(input())
ch1 = {}                                # ch1, ch2 를 딕셔너리로 초기화
ch2 = {}
for i in range(1,N+1):
    a = input().split()                 # 입력값 받기
    if not a[1] == '.':                 # 해당 인덱스 값이 . 이 아닐 경우
        ch1[a[0]] = a[1]                # ch1 또는 2의 a[0] 인덱스 번째 키 값에 a[1] or a[2] 추가
    if not a[2] == '.':
        ch2[a[0]] = a[2]

li = []                                 # li 는 계속 초기화 시켜주기
print(pre_order('A'))
li = []
print(in_order('A'))
li = []
print(post_order('A'))