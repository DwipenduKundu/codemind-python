def rotate(a, m, n):
	new = []
	if m > n:
	    m = m % n
	new = a[abs(n-m):]+a[:abs(n-m)]
	return new
n=int(input())
a=list(map(int,input().split()))
m=int(input())
a = rotate(a, m, n)
for i in a:
    print(i, end=" ")
