n=int(input())
arr=list(map(int,input().split()))
a=[]
if n%2==0:
    for i in range(n//2):
        a.append(arr[i])
        a.append(arr[n-i-1])
elif n%2!=0:
    for i in range(n//2):
        a.append(arr[i])
        a.append(arr[n-i-1])
    a.append(arr[n//2])
    a.append(0)
print(*a)