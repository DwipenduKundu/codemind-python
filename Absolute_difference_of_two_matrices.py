n=int(input())
m1=[]
m2=[]
for i in range(n):
    a=list(map(int,input().split()))
    m1.append(a)
for i in range(n):
    b=list(map(int,input().split()))
    m2.append(b)
for i in range(n):
    for j in range(n):
        print(abs(m1[i][j]-m2[i][j]),end='')
        if j!=n-1:
            print(" ",end='')
    print()