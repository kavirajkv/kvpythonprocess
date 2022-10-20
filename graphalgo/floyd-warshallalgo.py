#floyd-warshall algorithm implementation
def floydwarshall(mymat):
    (row,col,x)=mymat.shape
    infi=999
    short=np.zeros(shape=(row,col,col+1))
    for x in range(row):
        for y in range(col):
            short[x,y,0]=infi
            
    for x in range(row):
        for y in range(col):
            if mymat[x,y,0]==1:
                short[x,y,0]=mymat[x,y,1]
                
    for k in range(1,col+1):
        for i in range(row):
            for j in range(col):
                short[i,j,k]=min(short[i,j,k-1],short[i,k-1,k-1]+short[k-1,j,k-1])
                
    return short[:,:,col]

if __name__=='__main__':
    edges = [(0,1,9),(0,2,-4),(1,0,6),(1,3,2),(2,1,5),(3,2,1)]
    size = 4
    import numpy as np
    mat = np.zeros(shape=(size,size,2))
    for (i,j,w) in edges:
        mat[i,j,0] = 1
        mat[i,j,1] = w  
    print(mat)  
    print(floydwarshall(mat))