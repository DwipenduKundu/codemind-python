n=int(input())
l=1
for i in range(n):
    for j in range(n):
        if j>n-i-2:
            print(l,end='')
        else:
            print(' ',end='')
    for k in range(i):
        print(l,end='')
    l+=1
    print()