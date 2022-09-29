#insertion sort source code
def insertionsort(mylist):
    for i in range(1,len(mylist)):
        current=mylist[i]
        j=i-1
        while j>=0 and current<mylist[j]:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=current
    return mylist

if __name__=='__main__':
    my_list=[3,5,2,7,1]
    mysort=insertionsort(my_list)
    print(mysort)
    