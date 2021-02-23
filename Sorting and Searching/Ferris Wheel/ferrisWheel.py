n,x=map(int,input().split())
p=list(map(int,input().split()))
ans=0 
j=n 
p.sort()
for i in range(n) :
    if p[i]>x//2 :
        j=i 
        break
y=j-1 
while y>=0 and j<n :
    if p[y]+p[j]<=x :
        y-=1 
        j+=1 
        ans+=1 
    else :
        ans+=1 
        y-=2 
while j<n :
    ans+=1 
    j+=1 
while y>=0 :
    ans+=1 
    y-=2
print(ans)