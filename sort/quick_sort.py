def quick(L,start,end):
    pivot=L[0]
    start=pivot+1
    end=len(L)-1
    
    while start<=end:
        while start<=end and L[start]<=pivot:
            start=start+1
        while start<=end and L[end]>=pivot:
            end=end-1
            
        if start<end:
            L[start],L[end]=L[end],L[start]
            
    pivot,L[start]=L[start],pivot
    return start

def quicksort(Li,start,end):
    if start<end:
        q=quick(Li,start,end)
        quick(Li,start,q-1)
        quick(Li,q+1,end)



Li=[3,7,8,13,2,5]
qu=quicksort(Li,0,len(Li)-1)
print(qu)
    