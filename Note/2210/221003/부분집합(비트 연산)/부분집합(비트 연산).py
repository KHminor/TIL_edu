# n = 5
# li = [i for i in range(1,n+1)]
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(li[j], end=' ')
#     print()


# 음수 비트의 경우에는 0(00000000)과 -1(11111111)의 비트가 상반되므로
# 내가 생각하는 숫자의 +1 한것에 0과 1을 바꿔주면 된다.
# def bit(i):
#     output = ''
#     for j in range(7,-1,-1):
#         output += '1' if i & (1<<j) else '0'
#     print(output)
#
# for i in range(-5,6):
#     print('%3d = ' % i, end='')
#     bit(i)

#
# a = 0x10
# x = 0x01020304
# print(x)

# 빅 엔디안과 리틀 엔디안
# 빅 엔디안의 경우 메모리 주소공간을 0~n 으로 사용하여
#   디버그를 편하게 해 주는 경향이 있다고 한다.
# 반면 리틀 엔디안의 경우 메모리 주소공간을 n~0 으로 사용하여
#   메모리에 저장된 값의 하위 바이트들만 사용할 때
#   별도의 계산이 필요 없다는 장점이 있다.
