import  os
from collections import defaultdict
os.chdir('Day7')

class Graph:
    





'''lines = [l.split() for l in sys.stdin]
lines = [(l[1], l[7]) for l in lines]

steps = set([s[0] for s in lines] + [s[1] for s in lines])


def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]


order = ''
while steps:
    cand = list(next_step(steps, lines))
    cand.sort()

    n = cand[0]
    order += n
    steps.remove(n)
    lines = [(a, b) for (a, b) in lines if a != n]

print(order)'''


'''import os
os.chdir('Day7')
from collections import defaultdict

L = defaultdict(list)
Q = defaultdict(int)
for line in open('input'):
    steps = line.split()
    first = steps[1]
    last = steps[7]
    L[first].append([last])
    Q[last] += 1

for k in L:
    L[k] = sorted(L[k])
print (L, Q)

t = 0
EV = []
lst = []
def create_task(x):
    lst.append(x)
def work():
    global lst
    while len(EV) < 5 and lst:
        x = min(lst)
        lst = [y for y in lst if y!=x]
        print ('Starting {} at {}'.format(x,t))
        EV.append((t+61+ord(x)-ord('A'), x))

for k in L:
    if Q[k] == 0:
        create_task(k)
work()

while EV or lst:
    t, x = min(EV)
    print (t,x)
    EV =  [y for y in Q if y!= (t,x)]
    for y in L[x]:
        Q[y] -= 1
        if Q[y] == 0:
            create_task(y)
    work()

print (t)'''