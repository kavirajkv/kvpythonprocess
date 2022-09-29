#merge sort source code
def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=j=k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
               list1[k]=left_list[i]
               i=i+1
               k=k+1    
        while j<len(right_list):
              list1[k]=right_list[j]
              j=j+1
              k=k+1
    return list1         
    
if __name__=='__main__':
    mylist=[2,8,5,11,3,1,20,4]
    mysort=mergesort(mylist)
    print(mysort)