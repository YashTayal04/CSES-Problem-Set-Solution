# cook your dish here

def hanoi(n,i,j,k,l) :
    if n==1 :
        l.append((i,j))
    else :
        hanoi(n-1,i,k,j,l)
        l.append((i,j))
        hanoi(n-1,k,j,i,l)
        
n=int(input())
l=[]
hanoi(n,1,3,2,l)
print(len(l))
for i in l:
    print(i[0],i[1])