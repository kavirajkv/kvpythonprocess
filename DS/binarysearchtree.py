class Tree():
    #constructor which creates a node with value and left and right child or empty node if none is passed
    def __init__(self,val=None):
        self.value=val
        if self.value:
            self.left=Tree()
            self.right=Tree()
        else:
            self.left=None
            self.right=None
        return
    
    def isempty(self):
        #only empty node will become true
        return self.value==None
    
    def isleaf(self):
        #become true only if node contains value and left and right child empty
        return (self.value!=None and self.left.isempty() and self.right.isempty())
    
    #for traversing through every node and print the tree
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())
    #__str__ is a build in method which was used by print here when print(Tree()) is called this str method will return
    def __str__(self):
        return(str(self.inorder()))
    
    def insert(self,v):
        #if tree is empty then value will be inserted as head
        if self.isempty():
            self.value=v
            self.left=Tree()
            self.right=Tree()
            
        #if the given value is already present in the tree it will do nothing as tree wont contain duplicates
        if self.value==v:
            return
        #if v is smaller than root value then it will be inserted in the left side
        if v<self.value:
            self.left.insert(v)
            return
        if v>self.value:
            self.right.insert(v)    
            return
        
    def find(self,v):
        #this search if given element is present in the tree it is same like a binary search
        if self.isempty():
            return False
        if self.value==v:
            return True
        if v<self.value:
            return self.left.find(v)
        if v>self.value:
            return self.right.find(v)
    
    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return (self.left.minval())
        
    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return (self.right.maxval())
        
    #to create remove function we need to create makeempty,copyleft,copyright functions exclusively for creating remove function 
    def __makeempty(self):
        #for creating a empty node
        self.value=None
        self.left=None
        self.right=None
        return        
    def __copyleft(self):
        #this will copy the entire left child to the root(the current root)
        self.value=self.left.value
        self.right=self.left.right
        self.left=self.left.left
        return
    def __copyright(self):
        #same as copy left but it copy the the right child now
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right
        return
    def delete(self,v):
        if self.isempty():
            return
        if v<self.value:
            self.left.delete(v)
            return
        if v>self.value:
            self.right.delete(v)
            return
        if v==self.value:
            if self.isleaf():
                self.__makeempty()
            elif self.left.isempty():
                self.__copyright()
            elif self.right.isempty():
                self.__copyleft()
            else:
                self.value=self.left.maxval()
                self.left.delete(self.left.maxval())   
            return  
        
        

    
    
    
        
if __name__=='__main__':
    
    t=Tree()
    t.insert(5)
    t.insert(4)
    t.insert(1)
    t.insert(2)
    t.insert(6)
    print(t.find(1))
    print(t.minval())
    print(t.maxval())
    print(t)
    t.delete(4)
    print(t)
    
    