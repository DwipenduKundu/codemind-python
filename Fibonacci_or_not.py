x=int(input())
n=1000
a=0
b=1
arr=[]
if n==1:
	arr.append(a)
elif(n==2):
    arr.append(a)
    arr.append(b)
elif n>2:
	arr.append(a)
	arr.append(b)
	for i in range(2,n):
	    c=a+b
	    arr.append(c)
	    a=b
	    b=c
if x in arr:
    print("True")
else:
    print("False")