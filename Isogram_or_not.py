s=input()
f=0
for i in s:
    if s.count(i)!=1:
        f=1
        break
if f==0:
    print(True)
else:
    print(False)