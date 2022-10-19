#dijkstra's algorithm for finding shortest distance from a single source

import sys
def dijkstralist(mylist,s):
  infi=sys.maxsize #python will return the maximum value as it can be used as a infinity
  (visited,distance)=({},{}) 
  for x in mylist.keys():
    (visited[x],distance[x])=(False,infi)

  distance[s]=0
  for u in mylist.keys():
    nextd=min([distance[v] for v in mylist.keys() if not visited[v]]) #min distance of unvisited vertex 
    nextvlist=[x for x in mylist.keys() if (not visited[x]) and distance[x]==nextd] #vertices which are unvisited and minvalue in distance
    if nextvlist==[]:
      break
    nextv=min(nextvlist)
    visited[nextv]=True
    for (v,d) in mylist[nextv]:
      if not visited[v]:
        distance[v]=min(distance[v],distance[nextv]+d)
  return distance

if __name__=='__main__':
    dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
    size = 7
    mylst = {}
    for i in range(size):
        mylst[i] = []
    for (i,j,d) in dedges:
        mylst[i].append((j,d))
        
    print(dijkstralist(mylst,0))