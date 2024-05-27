import sys
import re
input = sys.stdin.readline

for _ in range(int(input())):
    chromosome = input().rstrip('\n')
    pattern = "[A-F]?A+F+C+[A-F]?$"
    if re.match(pattern,chromosome):
        print('Infected!')
    else: print('Good')