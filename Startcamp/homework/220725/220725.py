# print('*'.join('ssafy')) # s*s*a*f*y
# print(' '.join(['3', '5']))  # 3 5
# cafe = ['jsa', 'asdf', 'rlkdn']
# cafe.extend(['coffee'])
# cafe.extend('banana')
# cafe += ['apple']
# print(cafe)
# cafe.remove('b')
# cafe.clear()
# print(cafe)

ori = [1, 2, 3]
copy = ori
print(copy, ori)

copy[0] = 'hello'
print(ori, copy)