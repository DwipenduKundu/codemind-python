s=input()
a=list(s[::-1].split())
for i in range(len(a)):
    print(a[len(a)-i-1],end=' ')