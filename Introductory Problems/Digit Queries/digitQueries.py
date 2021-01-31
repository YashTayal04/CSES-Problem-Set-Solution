# cook your dish here
q=int(input())
while q>0 :
    k=int(input())
    x=1 
    j=1
    while x*9*j<k :
        k-=x*9*j 
        x*=10
        j+=1 
    p=k//j 
    x+=p-1 
    if k%j!=0 :
        x+=1 
        print(str(x)[k%j-1])
    else :
        print(str(x)[-1])
    q-=1