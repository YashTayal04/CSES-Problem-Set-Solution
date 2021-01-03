def power(a,b,m) :
    if b==0 :
        return 1 
    res=power(a,b//2,m)
    if b%2==0 :
        return (res*res)%m 
    else :
        return (res*res*a)%m 
n=int(input())
print(power(2,n,1000000007))