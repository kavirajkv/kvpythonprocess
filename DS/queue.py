#this queue can be very useful for graph oparations
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
    
    