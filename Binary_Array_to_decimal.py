n=int(input())
m=list(map(int,input().split())) 
s=0
for i in range(n):
    s+=m[i]*(2**(n-i-1))
print(s)