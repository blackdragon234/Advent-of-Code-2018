import os
os.chdir('Day3')
from collections import Counter

coordinateslist = Counter()
answer = set([])
duplicates = 0

#       splits the input in relevant parts. ID, @, XYcoordinates and size.
def makeanindex ()
f = open('input.txt')
for line in f:
        index = line.split(" ")
        answer.add(index[0])
        rectangleID = index[0][1:]
        rectangleSize = index[3].split("x")
        rectangleCoordinates = index[2].split(",")
        rectangleX = int(rectangleCoordinates[0])
        rectangleY = int(rectangleCoordinates[1][0:-1])
        rectangleW = int(rectangleSize[0]) 
        rectangleH = int(rectangleSize[1])

#       counts the squares of the rectangle and maps them to coordinates
#       if a coordinate is already 1 then the ID is cleared from the answer string
        while rectangleH > 0:
                Ycoordinate = rectangleY + rectangleH - 1
                while rectangleW > 0:
                        Xcoordinate = rectangleX + rectangleW - 1      
                        XYcoordinate = str(Ycoordinate)+ '-' + str(Xcoordinate)
                        if coordinateslist[XYcoordinate]  == 1:
                                coordinateslist[XYcoordinate] += 1
                                answer.discard(rectangleID)
                        else:
                                coordinateslist[XYcoordinate] += 1 
                        rectangleW -= 1
                rectangleH -= 1
                rectangleW = int(rectangleSize[0])
print (answer)