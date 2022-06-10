n=int(input())
count=0
add=0
sum=0
while n!=0:
    a=n%10
    n=n//10
    add+=1
    if a%2==0:
        count+=1
    elif a%2!=0:
        sum+=1
if add==sum:
    print("Odd")
elif add==count:
    print("Even")
else:
    print("Mixed")