s=input()
ans=1
curr=1
for i in range(1,len(s)) :
    if s[i]==s[i-1] :
        curr+=1
    else :
        ans=max(ans,curr)
        curr=1
print(max(ans,curr))