def selectionsort(mylst):
    #this loop is to initialize the first element
    for x in range(len(mylst)):
        minval=x
        #this loop will compare the initialized element with its next element
        for y in range(x+1,len(mylst)):
            if mylst[y]<mylst[minval]:
                minval=y
        #this will swap the minimum element to first element of unsorted array as x+1 is unsorted
        if x!=minval:
             mylst[x],mylst[minval]=mylst[minval],mylst[x]
    return mylst
if __name__=='__main__':
    mylist=[6,3,1,67,43,23,8]
    mysort=selectionsort(mylist)
    print(mysort)