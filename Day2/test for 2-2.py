import os
os.chdir('Day2')
from collections import Counter
answer = []
data = open('input.txt','r')

for line in data:
    baseline = set(line)
    for otherlines in data:
        nextline = set(otherlines)
        result = set.intersection(nextline, baseline)
        if len(result) == 2:
            answer.append(nextline-result)
            answer.append(baseline-result)
answer.sort()
print (answer[1])
