import sys
s = sys.stdin.readline()
s = s[:-1].lower()                      # 우선 모두 소문자로 변경
s_l = list(s)                           # 리스트로 담기

s_set = list(set(s))                    # 중복 제거 후 리스트로 담아서 순서대로 접근가능하게 만들기
# print(s_set)
# print(s_l)

cnt_li = []                             # 카운팅, 문자를 담을 리스트 초기화
str_li = []
max = result = max_idx= 0               # 가장 큰 값, 인덱스, 결과값 초기화

for i in range(len(s_set)):             # 중복을 제거한 리스트의 길이만큼 반복
    cnt = s_l.count(s_set[i])           # s_set[i] 값이 s_l 에 몇개 있는지 카운팅하기
    if cnt >= max:                      # cnt가 max 보다 크거나 같을 경우
        max = cnt                       # max 값에 cnt값 저장
        max_idx = i                     # 인덱스 또한 저장
        cnt_li.append(cnt)              # 카운팅 값 , 문자 함께 추가로 저장
        str_li.append(i)
# print(max)
# print(max_idx)
# print(cnt_li)
# print(str_li)
if cnt_li.count(max) == 1:              # 만약 가장 큰 게 하나 뿐이라면
    result = s_set[max_idx].upper()     # 가장 많은 개수를 가진 문자를 대문자로 변경 후 result 에 저장
else:                                   # 여러개의 경우
    result = '?'                        # result에 ? 저장
print(result)