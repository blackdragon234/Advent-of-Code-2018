import os, math
os.chdir('Day11')

fuelsquares = []
OGx = 1
OGy = 1

def getHundreds(number):
    hundreds = (number // 100)%10
    return hundreds

def getPower(x, y):
    Rack = 10 + x
    Power = getHundreds(((Rack * y) + 5177) * Rack) - 5
    return Power

while OGx <= 300:
    while OGy <= 300:
        aggregated = getPower(OGx, OGy) + getPower(OGx + 1, OGy) + getPower(OGx + 2, OGy) + getPower(OGx, OGy + 1) + getPower(OGx, OGy + 2) + getPower(OGx + 2, OGy + 2) + getPower(OGx + 1, OGy + 2) + getPower(OGx + 1, OGy + 1)+ getPower(OGx + 2, OGy + 1)
        fuelsquares.append(aggregated)
        OGy += 1
    OGy = 1
    OGx += 1

y = fuelsquares.index(max(fuelsquares)) % 300 + 1
x = fuelsquares.index(max(fuelsquares)) / 300
print (math.ceil(x), y)