n=int(input())
if n%4==0 or n%4==3 :
    print("YES")
    if n%4==0 :
        print(n//2)
        for i in range(1,n//2,2) :
            print(i,n-i+1,sep=" ",end=" ")
        print()
        print(n//2)
        for i in range(2,n//2+1,2) :
            print(i,n-i+1,sep=" ",end=" ")
        print()
    else :
        print(n//2+1)
        print("1 2",end=" ")
        for i in range(1,(n-3)//2,2) :
            print(i+3,n-i+1,sep=" ",end=" ")
        print()
        print(n//2)
        print("3",end=" ")
        for i in range(2,(n-3)//2+1,2) :
            print(i+3,n-i+1,sep=" ",end=" ")
        print()
else :
    print("NO")