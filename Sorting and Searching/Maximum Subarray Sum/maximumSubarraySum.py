n=int(input())
l=list(map(int,input().split()))
a=l[0]
c=l[0]
for i in l[1:] :
    c=max(0,c)
    c+=i 
    a=max(a,c)
print(a)