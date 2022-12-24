word='abcaaacabc'
pattern='ab'

i=0
j=0
lst=[]
while i<len(word) or j<len(pattern):
    if word[i]==pattern[j]:
        i=i+1
        j=j+1
        if j>(len(pattern)-1):
            j=0
            lst.append(i-len(pattern))
            if len(pattern)>1:
                i=i-1
    else:
        i=i+1
        j=0
    if i>=len(word):
        break
 
        
print(lst)