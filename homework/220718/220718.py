# 식별자 - 변수 이름 규칙

# 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
# 첫 글자에 숫자가 올 수 없음
# 길이 제한이 없고, 대소문자를 구별

# 예약어로 사용 불가능 한것을 알아내는 문장은

# import keyword
# print(keyword.kwlist)


# 진법 
# 2진수 : 0b
# 8진수: 0o
# 16진수 :0x


# import math
# math.isclose(a,b)


# 따옴표 안에 따옴표를 넣을 경우
#  ' 작은 따움표 안에는 "큰 따옴표를 안에 사용" ' 로 사용
# " 큰 따옴표 안에는 '작은 따옴표를 안에 사용' "



# Escape sequence
# 역 슬래시 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합 
# \n : 줄 바꿈
# \t : 탭
# \r : 캐리지 리턴 -> 커서를 맨 앞으로 보내는 것.
# \0 : 널 
# \\ : \  -> 역슬래시 자체를 사용하고 싶은 경우
# \' : 단일인용부호(')
# \" : 이중인용부호(")


# String Interpolation

# %s = strin
# %d = 정수
# %f = 소수 ex) 4.500000

# str.format()
# 'hello, {}'.format()

# 요즘 사용하는 방식은 f-string

# name = 'Kim'
# score = 4.5
# print( f'Hello, {name}! 성적은 {scroe}')

# 날짜 출력
# import datetime
# today = datetime.datetime.now()
# print(today)

# print(f'오늘은 {today :%y}년 {today : %m}월 {today :%d}일')
# ---> 오늘은 22년 07월 08일

# pi = 3.141592
# print(f'원주율은 {pi :.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
# ---> 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368