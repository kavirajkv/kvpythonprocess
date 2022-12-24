class AVLTree():
    #constructor which creates a node with value and left and right child or empty node if none is passed
    def __init__(self,val=None):
        self.value=val
        if self.value:
            self.left=AVLTree()
            self.right=AVLTree()
            self.height=1
        else:
            self.left=None
            self.right=None
            self.height=0
        return
    
    def isempty(self):
        #only empty node will become true
        return self.value==None
    
    
    #for traversing through every node and print the tree
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())
    #__str__ is a build in method which was used by print here when print(Tree()) is called this str method will return
    def __str__(self):
        return(str(self.inorder()))
    
    def rightrotate(self):
        v=self.value
        vl=self.left.value
        vr=self.right
        vll=self.left.left
        vlr=self.left.right
        newright=AVLTree(v)
        newright.left=vlr
        newright.right=vr
        self.value=vl
        self.left=vll
        self.right=newright
        return
    
    def leftrotate(self):
        v=self.value
        vr=self.right.value
        vrr=self.right.right
        vrl=self.right.left
        vl=self.left
        newleft=AVLTree(v)
        newleft.left=vl
        newleft.right=vrl
        self.value=vr
        self.left=newleft
        self.right=vrr
        return
    
    def updateheight(self):
        if self.isempty():
            return
        else:
            self.left.updateheight()
            self.right.updateheight()
            self.height=1+max(self.left.height,self.right.height)
            
    def rebalance(self):
        if self.left==None:
            hl=0
        else:
            hl=self.left.height
            
        if self.right==None:
            hr=0
        else:
            hr=self.right.height
        
        if hl-hr>1:
            if self.left.left.height>self.left.right.height:
                self.rightrotate()
            elif self.left.left.height<self.left.right.height:
                self.leftrotate()
                self.rightrotate()
            self.updateheight()
        
        if hl-hr<-1:
            if self.right.right.height>self.right.left.height:
                self.leftrotate()
            elif self.right.right.height<self.right.left.height:
                self.rightrotate()
                self.leftrotate()
            self.updateheight()
            
    def insert(self,v):
        if self.isempty():
            self.value=v
            self.left=AVLTree()
            self.right=AVLTree()
            self.height=1
            return
        if self.value==v:
            return
        if v<self.value:
            self.left.insert(v)
            self.rebalance()
            self.height=1+max(self.left.height,self.right.height)
        if v>self.value:
            self.right.insert(v)
            self.rebalance()
            self.height=1+max(self.left.height,self.right.height)
            
if __name__=='__main__':
    l=[5,1,2,4,6,7,3]           
    a=AVLTree()
    for i in l:
        a.insert(i)

    print(a)
    print(a.value)     
                    