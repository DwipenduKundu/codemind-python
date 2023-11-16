n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if i!=len(a)-1:
        if (a[i-1]%2==0 and a[i+1]%2==1) or (a[i-1]%2==1 and a[i+1]%2==0):
            c+=1
    if i==len(a)-1:
        if (a[i-1]%2==0 and a[0]%2==1) or (a[i-1]%2==1 and a[0]%2==0):
            c+=1
print(c)