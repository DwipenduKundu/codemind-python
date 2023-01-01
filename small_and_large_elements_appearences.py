str=list(input().split())
s=''
for i in str:
    s+=i
print(min(s),s.count(min(s)),max(s),s.count(max(s)),end=' ')