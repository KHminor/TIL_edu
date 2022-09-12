import sys
sys.stdin = open('input.txt')
st = []                         # 리스트 초기화
T = 10                          # 입력받을 값은 10개
for _ in range(T):
    namugy = int(input()) % 42  # 입력받은 정수를 42로 나눈 나머지를 namugy에 담기
    if namugy not in st:        # namugy의 값이 st안에 없다면 추가
        st.append(namugy)
cnt = 0                         # 카운트 할 cnt 초기화
for ln in st:
    cnt += 1                    # 요소의 개수 만큼 + 1
print(cnt)
33.33