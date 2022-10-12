#binary search program
def binarysearch(x,mylist):
    if mylist==[]:
        return 0
    
    mid=len(mylist)//2
    
    if x==mylist[mid]:
        return 1
    if x<mylist[mid]:
        return binarysearch(x,mylist[:mid])
    else:
        return binarysearch(x,mylist[mid:])
 
list1=list(x for x in  range(1,100))   
print(list1)
mynum=int(input('enter your number to search: '))
bisearch=binarysearch(mynum,list1)
print(bisearch)