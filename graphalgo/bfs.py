#program for BFS treaversal and finding parent,cost and shortest path using bfs
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

#adjecencylist for graph representation
edges=[(0,1),(1,2),(2,0),(0,4),(4,0),(4,3),(3,4),(3,6),(4,7),(7,4),(5,3),(6,5),(8,5),(7,8),(8,9),(9,8),(5,7)]

mylist={}
for i in range(10):
    mylist[i]=[]
for (i,j) in edges: 
    mylist[i].append(j)
print(mylist)

q=Queue()
visited={}
level={}
parent={}
bfs_traversal=[]
path=[]

for node in mylist.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
    
s=int(input('enter your root node: '))
visited[s]=True
level[s]=0
q.enq(s)

while not q.isempty():
    u=q.deq()
    bfs_traversal.append(u)
    for v in mylist[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            q.enq(v)
            
print('BFS traversal:',bfs_traversal)

#finding parent of a node
parentof=int(input('enter a vertex to find its parent from root: '))
print('its parent is:',parent[parentof])

#finding cost from root
costof=int(input('enter your node to ceck its cost from root: '))
print('its cost is: ',level[costof])

#path of a node from root
end=int(input('please enter your node see path from root: '))
while end is not None:
    path.append(end)
    end=parent[end]
path.reverse()    
print('The shortest path is: ',path)