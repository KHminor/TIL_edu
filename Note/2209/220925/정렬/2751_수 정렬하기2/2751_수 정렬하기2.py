# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    li.append(num)
li.sort()
for i in li:
    print(i)
