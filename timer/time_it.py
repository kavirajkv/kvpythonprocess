import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        myfunc=func(*args,**kwargs)
        end=time.time()
        print('execution time is: ',end-start)
        return myfunc
    return wrapper


@time_it
def sumofnum():
    num=0
    for x in range(1,100000):
        num+=x
    return num

p=sumofnum()
print(p)