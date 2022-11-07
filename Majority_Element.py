n=int(input())
a=list(map(int,input().split()))
j=[]
for i in range(n):
    if a.count(a[i])>n/2:
        j.append(a[i])
print(j[0])