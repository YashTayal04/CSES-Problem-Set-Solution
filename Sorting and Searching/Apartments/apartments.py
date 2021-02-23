n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
j=0
ans=0
for i in a : 
    while j<m and b[j]+k<i :
        j+=1 
    if j==m :
        break
    if i+k>=b[j] :
        ans+=1 
        j+=1 
print(ans)