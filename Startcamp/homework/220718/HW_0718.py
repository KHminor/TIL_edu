# 1. 
# pyhon 예약어: python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.

# =======================================================================

# import keyword
# print(keyword.kwlist)

# 2.
# 실수 비교: 아래와 같은 두 실수 값을 올바르게 비교하기 위한 코드를 작성하시오.

# =======================================================================

# import math
# num1 = 0.1 * 3
# num2 = 0.3
# print(math.isclose(num1,num2))

# =======================================================================

# 3.
# 이스케이프 시퀀스: (1)줄 바꿈, (2) 탭, (3) 백슬래시를 의미하는 이스케이프 시퀀스를 작성하시오.

# (1) = \n
# (2) = \t
# (3) = \\

# =======================================================================

# 4.
# String Interpolation(문자열을 변수를 활용하여 만드는 법): 
# 안녕, 철수야 를 sting interpolation 을 사용하여 출력하시오.

# name = "철수"

# %- 
# print("안녕 %s야" %name)

# format-
# print("안녕 {}야".format(name))

# f-
# print(f"안녕 {name}야")

# =======================================================================

# 5.
# 다음 중, 실행 시 오류가 발생하는 코드를 고르시오.
# (1) str(1)    (2)int('30')    (3)int(5)   (4)bool('50')   (5)int('3.5')

# 답은 (5)

# =======================================================================

# 6. 네모 출력
# 두 개의 정수 n과 m 이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별문자를 이용하여 출력
# 좀 간단하게 하고 싶은데...


# n = 5
# m = 9


# star = '*'*n*m
# print(star[:5])
# print(star[5:10])
# print(star[10:15])
# print(star[15:20])
# print(star[20:25])
# print(star[25:30])
# print(star[30:35])
# print(star[35:40])
# print(star[40:])

# =======================================================================

# 7.
# 이스케이프 시퀀스 응용 : print() 함수를 한 번만 사용하여 다음 문장을 출력하시오.

# print(""""파일은 c:\\Window\\Users\\내문서\\Python에 저장이 되었습니다."
# 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'""")

# =======================================================================

# 8.
# 근의 공식 : 다음은 이차 방정식의 근을 찾는 수식이다. 이를 파이썬 코드로 작성하시오.
# 맞나,,,?

# a = 4
# b = 4
# c = 4

# gn_gongsik_p, gn_gongsik_m = (-b + (b**2 - (4*a*c))**(1/2))/2*a, (-b - (b**2 - (4*a*c))**(1/2))/2*a 
# print(gn_gongsik_p,gn_gongsik_m)