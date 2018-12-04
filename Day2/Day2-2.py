import os
os.chdir('Day2')
from collections import Counter
answer = []
data = open('input.txt','r')

for line in data:
    baseline = set(line)
    for otherlines in data:
        nextline = set(otherlines)
        result = set.difference(nextline, baseline)
        if len(result) == 2:
            answer.append(nextline-result)
            answer.append(baseline-result)
print (','.join(answer[1]))
