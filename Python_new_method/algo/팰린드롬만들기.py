# import sys
# input = sys.stdin.readline
# s = input().rstrip('\n')
# ln = len(s) # 4

# cnt = 0
# while True:
#     if ln%2:
#         moc = ln//2
#         print(moc)
#         if moc >= len(s)-1:
#             print(len(s)*2-1)
#             break
#         else:
#             a = s[:cnt]+s[moc+1:]
#             print(s[:moc],'==?',a[::-1])
#             if s[:moc] == s[:cnt]+s[moc+1:]:
#                 print(len(s[:moc])*2+1)
#                 break
#     ln += 1
#     cnt += 1


import sys
input = sys.stdin.readline
s = input().rstrip('\n')

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break