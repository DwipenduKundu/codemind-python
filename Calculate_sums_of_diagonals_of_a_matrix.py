a=int(input())
sum=0
l=[]
for i in range(a):
    n=list(map(int,input().split()))
    l.append(n)
sum=0
sum1=0
for i in range(a):
    for j in range(a):
        if i==j:
            sum+=l[i][j]
for i in range(a):
    for j in range(a):
        if a-i-1==j:
            sum1+=l[i][j]
print("Principal Diagonal:{}".format(sum))
print("Secondary Diagonal:{}".format(sum1))