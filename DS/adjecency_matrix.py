#adjencymatrix for representing graph
import numpy as np
edges=[(0,1),(1,2),(2,0),(0,4),(4,0),(4,3),(3,4),(3,6),(4,7),(7,4),(5,3),(6,5),(8,5),(7,8),(8,9),(9,8)]

mymat=np.zeros(shape=(10,10))

for (i,j) in edges:
    mymat[i,j]=1
    
print(mymat)

#function to find neighbour

def neighbour(mat,i):
    neibh=[]
    (row,col)=mymat.shape
    for j in range(col):
        if mymat[i,j]==1:
            neibh.append(j)
    return neibh
if __name__=='__main__':
    nb=neighbour(mymat,2)
    print(nb)
    
