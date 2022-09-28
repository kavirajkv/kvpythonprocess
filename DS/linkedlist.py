#Empty node creation
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
#creating empty linked list
class LinkedList():
    def __init__(self):
        self.head=None
        
    #traversing or printing linkedlist
    def printll(self):
        if self.head is None:
            print('The linked list is empty')
            return
        else:
            node=self.head
            while node is not None:
                print(node.data)
                node=node.next
    #inserting node
    #inserting at begining
    def insertfirst(self,node):
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    #inserting at last
    def insertatlast(self,node):
        if self.head is None:
            self.head=node
        else:
            for currnode in self:
                pass
            currnode.next=node
    #inserting inbetween
    #insert after a target node
    def insert_after(self,target_node,newnode):
        if self.head is None:
            raise Exception('Linkedlist is empty')
        for node in self:
            if node.data==target_node:
                newnode.next=node.next
                node.next=newnode
        raise Exception('Element not found')
    
    #insert before the target node
    def insert_before(self,target_node,newnode):
        if self.head is None:
            raise Exception('Linkedlist is empty')
        if self.head.data==target_node:
            return self.insertfirst(newnode)
        prev_node=self.head
        for node in self:
            if node.data==target_node:
                prev_node.next=newnode
                newnode.next=node
                return
            prev_node=node
        raise Exception('Element not found')
    #deleting an element
    def remove(self,target):
        if self.head is None:
            raise Exception('Linkedlist is empty')
        if self.head==target:
            self.head.next=self.head
            return
        prev_node=self.head
        for node in self:
            if node.data==target:
                prev_node.next=node.next
                return
            prev_node=node
        raise Exception('Element not found')
ll=LinkedList()
ll.insertfirst(Node(6))
ll.insertatlast(Node(7))
ll.printll()
