import os, re
os.chdir('Day10')

lines = ''
P = []
min_x = 0
max_x = 0
min_y = 0
max_y = 0
seconds = 0
for line in open('input'):
    x,y,vx,vy = map(int, re.findall('-?\d+', line))
    P.append([x,y,vx,vy])

#update the minus and maximum values
def Update():
    min_x = min([x for x,y,_,_ in P])
    max_x = max([x for x,y,_,_ in P])
    min_y = min([y for x,y,_,_ in P])
    max_y = min([y for x,y,_,_ in P])

#get the Surface area of the bounding box
def GetSurface():
    width = max_x - min_x
    height = max_y - min_y
    surface = height * width
    return surface

#all points move
def secondPasses():
    for p in P:
        p[0] += p[2]
        p[1] += p[3]
    Update()



#one-time manual call to set the first and 2nd state.
Update()
Prevsurface = GetSurface()
secondPasses()
Currsurface = GetSurface()
print (Currsurface, Prevsurface, seconds)

while Currsurface < Prevsurface:
    Prevsurface = Currsurface()
    secondPasses()
    Currsurface = GetSurface()
print (Currsurface, seconds)
'''
i = min(positionx)
while i < max(positionx):
    j = min(positiony)
    while j < max(positiony):
        if j in positiony and positionx.index(i) == positiony.index(j):
            lines += '#'
        else:
            lines += ' '
        j += 1
    print(lines)
    i += 1
'''

