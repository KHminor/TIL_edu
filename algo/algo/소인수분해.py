# n = int(input())
# num = 2
# result = []
# while n >= num:
#     if not n%num: 
#         n //= num
#         result.append(num)
#     else: num += 1
# [print(i) for i in result]


n = int(input())
for i in range(2, int(n**0.5)+1):
    while not n%i:
        n //= i
        print(i)
if n != 1: print(n)