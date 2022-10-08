#adjecencylist for graph representation
edges=[(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(4,7),(3,5),(3,7),(5,6),(6,7)]

mylist={}
for i in range(8):
    mylist[i]=[]
for (i,j) in edges: 
    mylist[i].append(j)
        
print(mylist)

class Queue:
    def __init__(self):
        self.queue=[]
    def enq(self,a):
        self.queue.append(a)
    def deq(self):
        u=self.queue[0]
        self.queue=self.queue[1:]
        return u
    def isempty(self):
        return self.queue==[]
    
    
#topological sorting using adjacency list
def toposort(alist):
    indegree={}
    topo=[]
    
    #to find indegree of all vertices
    for x in alist.keys():
        indegree[x]=0
    for y in alist.keys():
         for z in alist[y]:
             indegree[z]=indegree[z]+1
             
    zerodegreeq=Queue()
    for u in alist.keys():
        if indegree[u]==0:
            zerodegreeq.enq(u)
    
    while not zerodegreeq.isempty():
        j=zerodegreeq.deq()
        topo.append(j)
        indegree[j]=indegree[j]-1
        for x in alist[j]:
            indegree[x]=indegree[x]-1
            if indegree[x]==0:
                zerodegreeq.enq(x)
    return topo

if __name__=='__main__':
    topologicalsort=toposort(mylist)
    print(topologicalsort)