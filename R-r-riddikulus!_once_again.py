def rotate(a, m, n):
	new = []
	if m > n:
	    m = m % n
	new = a[m:]+a[0:m]
	return new
n,m=map(int,input().split())
a=list(map(int,input().split()))
a = rotate(a, m, n)
for i in a:
    print(i, end=" ")