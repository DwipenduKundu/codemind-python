n=int(input())
for i in range(n):
    for j in range(n):
        if j==i or j==0:
            print("*",end="")
        elif i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()