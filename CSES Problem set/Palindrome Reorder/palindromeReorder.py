# cook your dish here
s = input()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
n = len(s)
if n % 2 == 0:
    f = 0
    for i in d.values():
        if i % 2 == 1:
            f = 1 
            break
    if f == 1:
        print("NO SOLUTION")
    else:
        l = [0] * n
        k = 0
        for i, j in d.items():
            for m in range(j // 2):
                l[k] = i 
                l[n - 1 - k] = i 
                k += 1
        print("".join(l))
else:
    f = 0
    l = [0] * n
    for j, i in d.items():
        if i % 2 == 1:
            if f == 1:
                f = 2
                break
            else:
                f = 1 
                l[n // 2 ] = j 
    if f % 2 == 0:
        print("NO SOLUTION")
    else:
        k = 0
        for i, j in d.items():
            for m in range(j // 2):
                l[k] = i 
                l[n - 1 - k] = i 
                k += 1
        print("".join(l))