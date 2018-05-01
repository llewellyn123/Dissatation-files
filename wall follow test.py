


mazename=""
mazesize=9
mazenum=999
import time
import numpy as np

#loads array bassed off the veribles above
mazearray=[[[0 for _ in range(10)] for _ in range(10)] for  _ in range (mazenum)]


#left number=dataset, right numbers= sloved? and =-time taken 
TestData=[[0] for _ in range(mazenum)]


#this is a recursive follow wall algrotithum that
#starts by checking if it has reached its destionantion
#checks too see if its hit a wall if it has it moves on to trying another place
# check if its been to that location before, if it has it tries another direction 
def search(maze,x, y):
    if x==8 and y==8:
        print("done")
        return 1
    elif maze[x][y] == 0:
        return False
    elif maze[x][y] == 3:
        return False
    
    maze[x][y] = 3

    # tries every direction unitill it finds a new space to go too,
    #repeats till it finds the end point
    if ((x < len(maze)-1 and search(maze,x+1, y))
        or (y > 0 and search(maze,x, y-1))
        or (x > 0 and search(maze,x-1, y))
        or (y < len(maze)-1 and search(maze,x, y+1))):
        return 1

    return False

#loads array and solves each maze after it saves the results 
for i in range(0,mazenum):
    mazename="maze/" +str(i)+".txt"
    mazearray[i]=np.loadtxt(mazename)
    start_time=time.time()
    search(mazearray[i],0,0)
    
    TestData[i]=round((time.time() - start_time),4)
    
np.savetxt("FloodData.txt",TestData,fmt="%.4f")
print(TestData)



