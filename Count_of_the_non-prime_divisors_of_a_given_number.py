n=int(input())
a=[]
a1=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in a:
    p=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            p=False
    if p==False:
        a1.append(i)
if 1 in a:
    a1.append(1)
print(len(a1))