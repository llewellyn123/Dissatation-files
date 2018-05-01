from mazelib import *
import random 
mazename=""
mazesize=9
mazenum=999
mazearray=[[[0 for _ in range(mazesize)] for _ in range(mazesize)] for  _ in range (mazenum)]

import numpy as np


#displays maze using "#" as walls

def displaymaze(a,maze):
    lineprint="#"
    print("############")
    for i in range (0,mazesize):
        for x in range(0,mazesize):
            if a[maze][i][x]==1:
                lineprint=lineprint+ " "
            elif a[maze][i][x]==2:
                lineprint=lineprint+"|"
            else:
                lineprint=lineprint+ "#"
        print (lineprint, "#")
        lineprint="#"
    print("############")

#loads maze

for i in range(0,mazenum):
    mazename="maze/" +str(i)+".txt"
    mazearray[i]=np.loadtxt(mazename)
x=0
mazeselect=0
#allows user to pick what maze they want too look at
while True:
    if x<=10:
        mazeselect=random.randrange(0,500)
        print(mazeselect)
        x=x+1
    if x>10:
        mazeselect=input("pick your maze")
        if mazeselect=="end":
            break

    for i in range (0,mazenum):
        if i==int(mazeselect):
            displaymaze(mazearray,i)
