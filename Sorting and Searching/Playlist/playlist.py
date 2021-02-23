n=int(input())
l=list(map(int,input().split()))
d={}
ans=1 
s=0
for i in range(n) :
    if d.get(l[i],-1)<s :
        d[l[i]]=i 
    else :
        ans=max(ans,i-s)
        s=d[l[i]]+1
        d[l[i]]=i 
#     print(ans,s)
# print(ans)
print(max(ans,n-s))