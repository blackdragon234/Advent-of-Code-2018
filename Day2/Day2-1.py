import os
os.chdir('Day2')
from collections import Counter
d = Counter()
duplicate = 0
triplet = 0

data = open('input.txt','r')

for line in data:
    d.clear()
    for c in line:
        d[c] +=  1
    if 2 in d.values():
        duplicate += 1
    if 3 in d.values():
        triplet += 1
print (duplicate, triplet)
checksum = duplicate * triplet
print (checksum)