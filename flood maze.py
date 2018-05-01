#same veribles as other code for creating the array to hold all the mazes in

mazename=""
mazesize=9
mazenum=9
mazearray=[[[0 for _ in range(10)] for _ in range(10)] for  _ in range (mazenum)]
mazearray2=[[[0 for _ in range(10)] for _ in range(10)] for  _ in range (mazenum)]
TestData=[[0] for _ in range(mazenum)]

import numpy as np
import time


#Flood fill algorithum
def DFS(x, y, visited, n, m, mat, destx, desty):
    if(x == destx and y == desty):
        visited[x][y]=5
        print("Solved")
        return True
    if(x >= n or y >= m):
        
        return False
    if(x <= -1 or y <= -1):
        
        return False
    if(visited[x][y] >1):
        
        return False
    if(mat[x][y] == 0):
        
        return False
    visited[x][y]=5

                              
    if DFS(x+1, y, visited, n, m, mat,  destx, desty) == True:
        return True
    if DFS(x-1, y, visited, n, m, mat,  destx, desty) == True:
        return True
    if DFS(x, y+1, visited, n, m, mat,  destx, desty) == True:
        return True
    if DFS(x, y-1, visited, n, m, mat,  destx, desty) == True:
        return True
    return False

#same code for running all the mazes and saving the results.

for i in range(0,mazenum):
    mazename="maze sample/" +str(i)+".txt"
    mazearray[i]=np.loadtxt(mazename)
    mazearray2[i]=np.loadtxt(mazename)
    start_time=time.time()
    DFS(0,0,mazearray[i],9,9,mazearray2[i],8,8)
    TestData[i]=round((time.time() - start_time),4)
    
np.savetxt("FloodData.txt",TestData,fmt="%.4f")
print(TestData)
