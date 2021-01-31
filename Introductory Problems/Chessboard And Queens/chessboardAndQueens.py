# cook your dish here
ans=0
def fun(l,r,c,d,u,i) :
    global ans 
    # print(ans)
    for j in range(8) :
        if i==7 :
            if c[j]==0 and d[i+j]==0 and u[i-j+7]==0 and l[i][j]=='.':
                ans+=1 
        else :
            if c[j]==0 and d[i+j]==0 and u[i-j+7]==0 and l[i][j]=='.':
                c[j]=1 
                d[i+j]=1 
                u[i-j+7]=1 
                fun(l,r,c,d,u,i+1)
                r[i]=0 
                c[j]=0 
                d[i+j]=0 
                u[i-j+7]=0
                    
l=[]
for i in range(8) :
    l.append(input())
r=[0]*8 
c=[0]*8 
d=[0]*15
u=[0]*15
fun(l,r,c,d,u,0)
print(ans)