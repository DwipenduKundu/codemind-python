n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=a+b
l=[]
for i in x:
    if i not in l and i not in a:
        l.append(i)
    if i not in l and i not in b:
        l.append(i)
print(len(l))