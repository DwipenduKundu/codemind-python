str=list(input().split())
small=0
large=0
for i in str:
    s=i
    large+=ord(max(s))
    small+=ord(min(s))
    sum=large-small
print(sum)