def quicksort(myl):
    elem=len(myl)
    if elem<2:
        return myl
    current=0
    
    for i in range(1,elem):
        if myl[i]<=myl[0]:
            current=current+1
            myl[i],myl[current]=myl[current],myl[i]
    myl[0],myl[current]=myl[current],myl[0]
    quicksort(myl[0:current])
    quicksort(myl[current+1:elem])
    return myl

if __name__=='__main__': 
    mylist=[3,2,7,9,1,6]
    mysort=quicksort(mylist)
    print(mysort)