import os
os.chdir('Day3')
from collections import Counter

testlist = Counter()

#       splits the input in relevant parts. ID, @, XYcoordinates and size.
def readthelines ():
        coordinateslist = Counter()
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
        return coordinateslist

testlist = readthelines()
answer = False

f = open('input.txt')
for line in f:
        if answer == True:
                print (rectangleID)
                break
        else:
                answer = True
                index = line.split(" ")
                rectangleID = index[0][1:]
                rectangleSize = index[3].split("x")
                rectangleCoordinates = index[2].split(",")
                rectangleX = int(rectangleCoordinates[0])
                rectangleY = int(rectangleCoordinates[1][0:-1])
                rectangleW = int(rectangleSize[0]) 
                rectangleH = int(rectangleSize[1])
                while rectangleH > 0 and answer:
                        Ycoordinate = rectangleY + rectangleH - 1
                        while rectangleW > 0 and answer:
                                Xcoordinate = rectangleX + rectangleW - 1
                                XYcoordinate = str(Ycoordinate)+ '-' + str(Xcoordinate)
                                if testlist[XYcoordinate] != 1:
                                        answer = False
                                rectangleW -= 1
                        rectangleH -= 1
                        rectangleW = int(rectangleSize[0])
