n,m=map(int,input().split())
h=list(map(int,input().split()))
p=list(map(int,input().split()))
h.sort()
ls=[0]*n
li=[i-1 for i in range(n)]
for i in p:
    l=0 
    r=n-1
    ans=l
    while l<=r :
        m=(l+r)//2 
        if h[m]>i :
            r=m-1 
        else :
            ans=m 
            l=m+1
    m=ans
    if h[m]<=i :
        if ls[m]==0 :
            print(h[m])
            ls[m]=-1 
            if m>0 :
                if ls[m-1]==0 :
                    li[m]=m-1 
                else :
                    li[m]=li[m-1]
        else :
            x=m
            while ls[m]!=0 and li[m]>=0 :
                m=li[m]
            # print(x,m)
            while x!=m :
                temp=x 
                x=li[x]
                li[temp]=m
                # x,li[x]=li[x],m
            if ls[m]==0 :
                print(h[m])
                ls[m]=-1 
                if m>0 :
                    if ls[m-1]==0 :
                        li[m]=m-1 
                    else :
                        li[m]=li[m-1]
            else :
                print(-1)
    else :
        print(-1)
    # print(ls,li)
        