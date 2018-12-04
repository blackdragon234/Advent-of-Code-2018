import os
os.chdir('Day2')
from collections import Counter
answer = []
data = open('test2.txt','r')

for line in data:
    baseline = set(line)
    data_comparison = open('test2.txt', 'r')
    for otherlines in data_comparison:
        nextline = set(otherlines)
        result = set.difference(nextline, baseline)
        if len(result) == 1:
            print(line, otherlines)