class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None
    
class DoublyLL:
  def __init__(self):
    self.head=None

  def traverse(self):
    if self.head==None:
      print('list is empty')
    else:
      a=self.head
      while a is not None:
        print(a.data,end='-->')
        a=a.next
      
  def reverse_traverse(self):
    if self.head==None:
       print('list is empty')
    else:
      a=self.head
      while a.next is not None:
        a=a.next
      while a is not None:
        print(a.data,end='-->')
        a=a.prev
       
  def insert_front(self,data):
    newnode=Node(data)
    if self.head==None:
      self.head=newnode
    else:
      a=self.head
      a.prev=newnode
      newnode.next=a
      self.head=newnode

  def insert_last(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      a=self.head
      while a.next is not None:
        a=a.next
      a.next=newnode
      newnode.prev=a

  def insert_at(self,position,data):
    newnode=Node(data)
    if position==0:
      return self.insert_front(data)
    else:
      a=self.head
      for i in range(1,position-1):
        a=a.next
      newnode.prev=a
      newnode.next=a.next
      a.next.prev=newnode
      a.next=newnode
      
  def del_at_front(self):
    if self.head==None:
      print('list is empty')
    else:
      a=self.head
      self.head=a.next
      a.next=None
      self.head.prev=None

  def del_at_end(self):
    if self.head==None:
      print('list is empty')
    else:
      a=self.head
      while a.next is not None:
        a=a.next
      a.prev.next=None
      a.prev=None

  def removenode(self,key):
    if key==self.head.data:
      return self.del_at_front()
    else:
      a=self.head
      while a is not None:
        if a.data==key:
          a.next.prev=a.prev
          a.prev.next=a.next  
        a=a.next
    
      
if __name__=='__main__':
    dll=DoublyLL()
    dll.insert_front(4)
    dll.insert_front(3)
    dll.insert_last(6)
    dll.insert_last(7)
    dll.insert_at(2,5)
    dll.traverse()
    dll.del_at_front()
    dll.del_at_end()
    dll.removenode(4)

    print()
    dll.traverse()
    print()
    dll.reverse_traverse()
