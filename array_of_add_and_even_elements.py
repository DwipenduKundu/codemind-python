n=int(input())
a=list(map(int,input().split()))
ae=[]
ao=[]
for i in range(n):
    if a[i]%2==1:
        ao.append(a[i])
    elif a[i]%2==0:
        ae.append(a[i])
for i in range(len(ao)):
    print(ao[i],end=' ')
for i in range(len(ae)):
    print(ae[i],end=' ')