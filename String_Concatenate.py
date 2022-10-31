n=input()
m=input()
s=n+m
a=list(s)
a.sort()
for i in range(len(a)):
    print(a[i],end="")