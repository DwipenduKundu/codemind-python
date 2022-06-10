n=int(input())
c="A"
for i in range(1,n+1):
    for j in range(1,n+1):
        print(c,end=" ")
    c=chr(ord(c) + 1)
    print()