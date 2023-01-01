str=list(input().split())
for i in str:
    small=0
    large=0
    s=i
    large+=ord(max(s))
    small+=ord(min(s))
    sum=large-small
    print(sum,end=' ')