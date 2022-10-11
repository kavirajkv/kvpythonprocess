#initaializaton of node for a singly linked list
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

#class for a initiation of singlylinked list
class SingleLL:
  def __init__(self):
    self.head=None
  #printsll function can be used to traverse the list
  def printsll(self):
    if self.head==None:
      print('list is empty')
    else:
      n=self.head
      while n is not None:
        print(n.data,end='-->')
        n=n.next
        
  def insert_at_first(self,data):
    newnode=Node(data)
    if self.head==None:
      self.head=newnode
    else:
      newnode.next=self.head
      self.head=newnode
  
  def insert_at_last(self,data):
    newnode=Node(data)
    if self.head==None:
      self.head=newnode
    else:
      n=self.head
      while n.next is not None:
        n=n.next
      n.next=newnode

  def insertat(self,position,data):
    newnode=Node(data)
    if position==0:
      return self.insert_at_first(data)
    n=self.head
    for i in range(1,position):
      n=n.next
    newnode.next=n.next
    n.next=newnode

  def removenode(self,key):
    if self.head==None:
        print('list is empty')
    prev=self.head
    a=self.head.next
    if prev.data==key:
      self.head=a
      a=None
    else:
      while a is not None:
        if a.data==key:
          prev.next=a.next
        prev=prev.next
        a=a.next
     
if __name__=='__main__':
    sll=SingleLL()
    sll.insert_at_first(6)
    sll.insert_at_first(5)
    sll.insert_at_last(7)
    sll.insert_at_last(10)
    sll.insertat(3,8)
    sll.insertat(4,9)
    sll.insertat(0,4)
    sll.printsll()
    sll.removenode(10)
    sll.removenode(4)
    sll.removenode(7)
    print()
    sll.printsll()