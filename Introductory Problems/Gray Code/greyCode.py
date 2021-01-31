# cook your dish here
n=int(input())
l=['0','1']
for i in range(n-1) :
    l1=list(l[::-1])
    for i in range(len(l)) :
        l[i]='0'+l[i]
    for i in range(len(l1)) :
        l1[i]='1'+l1[i]    
    l.extend(l1)
for i in l :
    print(i)
    