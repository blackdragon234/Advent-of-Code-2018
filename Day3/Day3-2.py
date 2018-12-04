import os
os.chdir('Day3')
from collections import Counter

coordinateslist = Counter()
duplicates = 0



f = open('input.txt')
for line in f:
    index = line.split(" ")
    rectangleSize = index[3].split("x")
    rectangleCoordinates = index[2].split(",")
    rectangleX = int(rectangleCoordinates[0])
    rectangleY = int(rectangleCoordinates[1][0:-1])
    rectangleW = int(rectangleSize[0]) 
    rectangleH = int(rectangleSize[1])
    while rectangleH > 0:
        Ycoordinate = rectangleY + rectangleH - 1
        while rectangleW > 0:
            Xcoordinate = rectangleX + rectangleW - 1
            XYcoordinate = str(Ycoordinate)+ '-' + str(Xcoordinate)
            coordinateslist[XYcoordinate] += 1
            rectangleW -= 1
        rectangleH -= 1
        rectangleW = int(rectangleSize[0])
        for x in coordinateslist:
                if coordinateslist[x] > 1:
                        duplicates += 1
                else:
                        answer = line

print (duplicates)
print (answer)