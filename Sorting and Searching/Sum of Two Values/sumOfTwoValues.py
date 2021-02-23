# cook your dish here
n,x=map(int,input().split())
ls=list(map(int,input().split()))
l=[(ls[i],i+1) for i in range(n)]
l.sort()
i=0
j=n-1
while i<j :
    if l[i][0]+l[j][0]==x :
        break
    if l[i][0]+l[j][0]>x :
        j-=1 
    else :
        i+=1 
if i!=j and l[i][0]+l[j][0]==x :
    print(l[i][1],l[j][1])
else :
    print("IMPOSSIBLE")