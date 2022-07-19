score = {
'python': 80,
'django': 89,
'web': 83
}

score["algorithm"] = 90
score['python'] = 85
sum_score = score.values()
sum = sum(sum_score)
print(sum)

cnt = len(score.keys())

print(sum/cnt)
