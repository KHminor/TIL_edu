import sys
n,l,d = map(int,input().split())

e_song,e_rest,bell = 0,0,0
for _ in range(n):
    e_song += l
    e_rest = e_song+5
    while e_rest > bell:
        if e_song <= bell < e_rest:
            print(bell)
            sys.exit(0)
        else: bell += d
    e_song = e_rest
print(bell)

# (0+5)+5: 10 -> 5 <= x < 10
# (10+5)+5: 20 -> 15 <= x < 20
# (28+5)+5: 42 -> 37 <= x < 42

# (0+9)+5: 14 -> 9 <= x < 14
# (14+9)+5: 28 -> 23 <= x < 28
# (28+9)+5: 42 -> 37 <= x < 42
