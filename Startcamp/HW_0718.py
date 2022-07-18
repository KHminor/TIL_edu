 
from multiprocessing.sharedctypes import Value


score = {'python' : 80, 'django' : 89, 'wdb' : 83}

# 1.
score['algorithm'] = 90

# 2.
score['python'] = 85

# 3.
avg = sum(score.values())/ len(score.keys())
print(avg)




