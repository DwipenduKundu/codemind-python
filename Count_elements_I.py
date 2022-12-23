n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=a+b
l=[]
for i in x:
    if i not in l and i in a and i in b:
        l.append(i)
print(len(l))