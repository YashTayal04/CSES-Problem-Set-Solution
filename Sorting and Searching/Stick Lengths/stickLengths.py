# cook your dish here
n=int(input())
p=list(map(int,input().split()))
p.sort()
if n%2==1 :
    c=0 
    for i in p:
        c+=abs(i-p[n//2])
    print(c)
else :
    c0=0 
    c1=0 
    for i in p:
        c0+=abs(i-p[n//2])
        c1+=abs(i-p[n//2-1])
    print(min(c0,c1))