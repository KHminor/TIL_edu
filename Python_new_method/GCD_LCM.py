# 유클리드 호제법

# 최대 공약수
def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

# 최소 공배수
def LCM(x,y):
    return (x*y)//GCD(x,y) # x*y 를 최대공약수로 나눈 몫이 최소 공배수.


# 10, 12   => 12, 10 => 10, 2 => 2, 0