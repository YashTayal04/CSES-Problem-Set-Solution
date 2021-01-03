# cook your dish here
ans = 1000000000
def fun(s1, s2, i, n):
    global ans
    if i == n:
        ans = min(ans, abs(s1 - s2))
    else:
        fun(s1 + l[i], s2, i+1, n)
        fun(s1, s2 + l[i], i+1, n)


n = int(input()) 
l = list(map(int, input().split()))
fun(0, 0, 0, n)
print(ans)