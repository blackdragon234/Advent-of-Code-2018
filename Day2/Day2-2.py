import os
os.chdir('Day2')
from collections import Counter

data = open('test2.txt','r')

for line in data:
    baseline = line
    nextline = next(data)
    result = first_difference(baseline, nextline)
    for c in line:
        d[c] +=  1
    if 2 in d.values():
        duplicate += 1
    if 3 in d.values():
        triplet += 1

def first_difference(str1, str2):
    for a, b in zip(str1, str2):
        if a != b:
            return a+b
#        if baseline almost = line then position = data.tell()
print (duplicate, triplet)
checksum = duplicate * triplet
print (checksum)