################################################################
# this is a program to generate 2d mazes and save it too a folder called
# "maze"


###############################################################

#mazelib is for the maze generatoin algorithum

#numpy is for saving the mazes to a folder

from mazelib import *
import numpy as np

#maze size
mazesize=11
mazesize2=9

#number of mazes generated
mazenum=500

#maze naming using format "maze/" + i + ".txt"
mazename=""

#array generation
mazearray=[[[0 for i in range(mazesize)] for i in range(mazesize)] for  i in range (mazenum)]

mazearray2=[[[0 for i in range(mazesize2)] for i in range(mazesize2)] for  i in range (mazenum)]

# makes the maze using the division method
m = Maze()
m.generator = Division(5, 5)

#cycles through the required mazes and creates and saves the array    
for i in range (0, mazenum):
    x= np.array(mazearray[i])

    y=np.array(mazearray2[i])

    m.generate()
    x=m.grid
    print(x)

#due to the way the libabry generates using 1 as walls and the net work
#uses 0 i have to flip them round in the array 
    for f in range (1, mazesize-1):
        for z in range(1,mazesize-1):
            if x[f][z]==0:
                y[f-1][z-1]=1
            else:
                y[f-1][z-1]=0
    print(y)
    x=y

    
    mazename="maze train/" +str(i)+".txt"
    print(mazename)

    
    np.savetxt(mazename, y, fmt="%5.0f")

