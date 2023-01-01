str=list(input().split())
v=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in str:
    s=i
    if s[0] in v and s[-1] not in v and s[-1].isalpha()==True:
        count+=1
print(count)