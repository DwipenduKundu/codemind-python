n=int(input())
c=chr(64+n)
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(c,end=" ")
    c=chr(ord(c) - 1)
    print()