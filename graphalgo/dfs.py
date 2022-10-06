#adjecencylist for graph representation
edges=[(0,1),(1,2),(2,0),(0,4),(4,0),(4,3),(3,4),(3,6),(4,7),(7,4),(5,3),(6,5),(8,5),(7,8),(8,9),(9,8),(5,7)]

mylist={}
for i in range(10):
    mylist[i]=[]
for (i,j) in edges: 
    mylist[i].append(j)
        
print(mylist)

visited=set()

def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)
    

dfs(4,visited,mylist)
