#implementation belman-ford algorithm 
import sys
def bellmanfordalgo(mylist,s):
    infi=sys.maxsize
    distance={}
    for x in mylist.keys():
        distance[x]=infi
        
    distance[s]=0
    
    for i in mylist.keys(): #for relaxing n-1 times 
        for u in mylist.keys():
            for (v,d) in mylist[u]:
                distance[v]=min(distance[v],distance[u]+d)
                
    return distance    

if __name__=='__main__':
    edges = [(0,1,6),(0,2,4),(0,3,5),(2,1,-2),(3,2,-2),(1,4,-1),(2,4,3),(3,5,-1),(4,5,3)]
    size = 6
    mylst = {}
    for i in range(size):
        mylst[i] = []
    for (i,j,d) in edges:
        mylst[i].append((j,d))
        
    print(bellmanfordalgo(mylst,0))