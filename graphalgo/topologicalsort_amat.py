#adjencymatrix for representing graph
import numpy as np
edges=[(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(4,7),(3,5),(3,7),(5,6),(6,7)]

mymat=np.zeros(shape=(8,8))

for (i,j) in edges:
    mymat[i,j]=1
    
print(mymat)

#topological sort using adjacency matrix
def toposort(amat):
    #initializing indegree and list store toposort
    (row,col)=amat.shape
    indegree={}
    topo=[]
    #finding incoming degrees of all vertices
    for c in range(col):
        indegree[c]=0
        for r in range(row):
            if amat[r,c]==1:
                indegree[c]=indegree[c]+1
    #finding '0' degree vertex
    for i in range(row):
        temp=[]
        for k in range(col):
            if indegree[k]==0:
                temp.append(k)
        j=min(temp)
        topo.append(j)
        indegree[j]=indegree[j]-1
        #updating indegrees of other vertices
        for k in range(col):
            if amat[j,k]==1:
                indegree[k]=indegree[k]-1  
                
    return topo


if __name__=='__main__':
    topologialsort=toposort(mymat)
    print(topologialsort)