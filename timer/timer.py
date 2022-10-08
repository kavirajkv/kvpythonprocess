import time

class Timer():
    def __init__(self):
        self.starttime= None
        self.endtime= None
        
    def start(self):
        self.starttime=time.time()
        return self.starttime
        
    def end(self):
        self.endtime=time.time()-self.starttime
        return self.endtime
        
    def __str__(self):
        return(str((self.endtime)*1000))
    
t=Timer()    
t.start()
num=0
for x in range(1,100000):
    num+=x
print(num)
t.end()
print(t)