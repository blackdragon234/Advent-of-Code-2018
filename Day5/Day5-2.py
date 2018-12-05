import os
os.chdir('Day5')

checklist = []
resultchars = []
theshortest = 9999999999
f = open('input.txt')
for polymer in f:
    OGpolymer = polymer

def removechars(polymer, cappa, lowa):
    chars = []
    for c in polymer:
        if ord(c) != cappa and ord(c) != lowa:
            chars.append(ord(c))
    return(chars)

def collapsee(chars):
    d = 0
    while d < len(chars) - 1:
        if chars[d] == chars[d+1]+32 or chars[d] == chars[d+1]-32:
            del(chars[d])
            del(chars[d])
            d = d-2
        d += 1
    return(len(chars))

for alpha in range(26):
    cappa = 65 + alpha
    lowa = 97 + alpha
    polylength = collapsee(removechars(OGpolymer, cappa, lowa))
    if polylength < theshortest:
        theshortest = polylength
print (theshortest)