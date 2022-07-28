import random
# [표현식] => [num for num in range(10)]
# num  => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2-3

number_lines = [sorted(list(random.sample(range(1, 46), 6))) for i in range(5)]
print(number_lines)