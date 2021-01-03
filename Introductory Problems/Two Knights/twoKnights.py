n=int(input())
for i in range(1,n+1) :
    if i==1 :
        print(0)
    elif i==2 :
        print((4*3)//2)
    elif i==3 :
        x=i**2 
        print(x*(x-1)//2 - 8*1)
    else :
        x=i**2 
        y=(i-4)**(2)
        print(x*(x-1)//2 - (y*8 + 4*2 + 8*3 + 4*(i-4)*4 + 4*4 + 4*(i-4)*6)//2)