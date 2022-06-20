n=int(input())
m=int(input())
for i in range(n,m+1):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count==1:
        print(i)