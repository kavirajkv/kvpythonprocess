#class for union find data structure as python don't have inbuilt this type data structure
class unionfind():
    parent={}
    
    rank={} #for tracking depth
    def __init__(self,uni):
        self.uni=uni    
    def makeunionfind(self):
        #creating distinct set for each element in uni
        for i in self.uni:
            self.parent[i]=i
            self.rank[i]=0
            
    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])    
      
    def union(self,a,b):
        x=self.find(a)
        y=self.find(b)
        
        if x==y:
            return
        if self.rank[x]>self.rank[y]:
            self.parent[y]=x
            self.rank[x]=self.rank[x]+1
        elif self.rank[x]<self.rank[y]:
             self.parent[x]=y
             self.rank[y]=self.rank[y]+1   
        else:
            self.parent[x]=y
            self.rank[y]=self.rank[y]+1
    
    def printunion(self):
        l=[self.find(i) for i in self.uni]
        return l
    
    
if __name__=='__main__':
    
    u=[1,2,3,4,5]            
    uf=unionfind(u)
    m=uf.makeunionfind()
    q=uf.printunion()
    print(q) 
    uf.union(1,2)
    uf.union(2,3)
    uf.union(1,3)
    uf.union(3,4)
    uf.union(4,5)
    n=uf.printunion()
    print(n)
          
                   
               