# cook your dish here
t = int(input())
while t > 0:
    a, b = map(int, input().split())
    if a == b:
        if a % 3 == 0:
            print("YES")
        else:
            print("NO")
    elif max(a, b) - min(a, b) <= min(a, b) and (2 * min(a, b) - max(a, b)) % 3 == 0:
        print("YES")
    else:
        print("NO")
    t -= 1