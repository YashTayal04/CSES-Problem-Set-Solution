t=int(input())
while t>0:
    y,x=map(int,input().split())
    if y>=x :
        a=(y-1)**2
        if y%2==1 :
            print(a+x)
        else :
            print(a+y+y-x)
    else :
        a=(x-1)**2
        if x%2==0 :
            print(a+y)
        else :
            print(a+x+x-y)
    t-=1