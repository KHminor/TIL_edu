n = int(input())
dna = list(input())
chart = {
    "AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", 
    "GA" : "C", "GG" : "G", "GC" : "T", "GT" : "A", 
    "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G", 
    "TA" : "G", "TG" : "A", "TC" : "G", "TT" : "T"
    }

result = chart["".join(dna[n-2:])]
n -= 3
while n != -1:
    result = chart[dna[n]+result]
    n-=1
print(result)