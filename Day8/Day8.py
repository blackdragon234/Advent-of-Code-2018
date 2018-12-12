import os
os.chdir('Day8')

with open('easy') as line:
    it = line.split(' ')
    everything = [int(x) for x in it]

childlist = []
metadatalist = []

for i in everything:
    pos = everything.index(i)