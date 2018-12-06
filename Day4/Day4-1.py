import os
os.chdir('Day4')
from collections import Counter

f = open('input')
dutieslist = []

def sleepyguardslist(dutieslist):
    sleepyend = 0
    sleepycounter = Counter()
    for data in range(len(dutieslist) - 1):
        line = dutieslist[data].split((' '))
        if len(line) == 6:
            currentguard = line[3]
        if len(line) != 6:
            if line[2] == 'falls':
                sleepystart = int((line[1][3:-1]))
                continue
            if line[2] == 'wakes':
                sleepyend = int((line[1][3:-1]))
                sleepytime = sleepyend - sleepystart
                sleepycounter[currentguard] = sleepycounter[currentguard] + sleepytime
    return list(sleepycounter.most_common(1))[0]

def sleepiestminutes(guardnumber,dutieslist):
    sleepyminutesc = Counter()
    rightguard = False
    for data in range(len(dutieslist) - 1):
        line = dutieslist[data].split((' '))
        if len(line) == 6:
            if line[3] == guardnumber:
                rightguard = True
                continue
            else:
                rightguard = False
        if rightguard == True and line[2] == 'falls':
            sleepystartminute = int(line[1][3:-1])
            line = dutieslist[data+1].split((' '))
            sleepyendminute = int(line[1][3:-1])
            while sleepyendminute >= sleepystartminute:
                sleepyendminute -= 1  
                sleepyminutesc[sleepyendminute] += 1
    return sleepyminutesc.most_common(1)

for line in f:
    dutieslist.append(line)
list.sort(dutieslist)
sleepiestguard = sleepyguardslist(dutieslist)
sleepiestmin = sleepiestminutes(sleepiestguard[0],dutieslist)
print("The sleepiestguard =")
print(sleepiestguard)
print("His most sleepyminute =")
print(sleepiestmin)