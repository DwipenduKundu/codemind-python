n=int(input())
for i in range(n,0,-1):
    k=n-i+1
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()