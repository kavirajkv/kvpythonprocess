def gcd(a,b):
    (a,b)=(max(a,b),min(a,b))
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
    
if __name__=='__main__':
    x=int(input())
    y=int(input())
    ans=gcd(x,y)
    print(ans)