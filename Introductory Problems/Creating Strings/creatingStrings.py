# cook your dish here
def fun(s,t,l) :
    if len(t)==1 :
        l.append(s+t)
    else :
        n=len(t)
        for i in range(n) :
            a=""
            if i>0 :
                a+=t[:i]
            if i<n-1 :
                a+=t[i+1:]
            fun(s+t[i],a,l)

s=input()
l=[]
fun("",s,l)
l=list(set(l))
l.sort()
print(len(l))
for i in l:
    print(i)