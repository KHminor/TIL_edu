import random
# [표현식] => [num for num in range(10)]
# num  => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2-3
n = 5
a = [list(random.sample(1, 46)) for _ in range(n)]
print(a)