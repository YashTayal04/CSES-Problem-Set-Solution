# cook your dish here
n=int(input())
l=[]
for i in range(n) :
    a,b=map(int,input().split())
    l.append((b,a))
l.sort()
c=1 
last=l[0][0]
for i in l[1:] :
    if i[1]>=last :
        c+=1 
        last=i[0]
print(c)