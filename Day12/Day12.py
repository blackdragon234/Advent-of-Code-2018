import os, re
os.chdir('Day12')

pots = []
nextstate = []
growthconditions = []

f = open('input')
for line in f:
    if len(line) >= 13:
        initialline = line.split(' ')[2][:-1]
        for i in initialline:
            pots.append(i)
        print(''.join(pots))
        nextstate = pots.copy()
    else:
        if len(line) > 2:
            growthconditions.append(line.split(' ')[0])
            growthconditions.append(line.split(' ')[2][:-1])

def nextgeneration(pots,nextstate):
    generations = 0
    while generations < 20: 
        spread = ''
        for i in range(len(pots[2:-2])):
            if i >= 2:
                spread = pots[i-2] + pots[i-1]+ pots[i] + pots[i+1] + pots[i+2]
                indexlocation = growthconditions.index(spread)
                nextstate[i] = growthconditions[indexlocation+1]
            else:
                continue
        pots.clear
        pots= nextstate.copy()
        generations += 1
    aggr = 0
    for i in range(len(pots)):
        if pots[i] == "#":
            aggr += i - 2
        else:
            continue
    print(''.join(pots))
    print(aggr)

nextgeneration(pots, nextstate)


        

