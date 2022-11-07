f=input()
n=[]
for i in range(len(f)):
    if f[i].isnumeric()==True:
        n.append(int(f[i]))
v=[]
a1=[]
for i in n:
    if i not in v:
        a=[]
        for j in range(1,i+1):
            if i%j==0:
                a.append(j)
        if sum(a) in n:
            a1.append(i)
    v.append(i)
if len(a1)>0:
    a1.sort()
    for i in a1:
        print(i,end=' ')
elif len(a1)==0:
    print(-1)
