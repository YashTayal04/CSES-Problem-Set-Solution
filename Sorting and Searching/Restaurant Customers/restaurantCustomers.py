import sys 
input=sys.stdin.readline
n=int(input())
a=[]
d=[]
for i in range(n) :
    x,y=map(int,input().split())
    a.append(x)
    d.append(y)
a.sort()
d.sort()
c=0
m=0
i=0
j=0
while i<n :
    if a[i]<=d[j] :
        c+=1 
        m=max(m,c)
        i+=1 
    else :
        c-=1 
        j+=1
print(m)