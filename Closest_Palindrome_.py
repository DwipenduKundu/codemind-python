a=int(input())
np=a+1
while 1:
    if np==int(str(np)[::-1]):
        f1=np
        break
    np+=1
np=a-1
while 1:
    if np==int(str(np)[::-1]):
        f2=np
        break
    np-=1
if abs(a-f2)>abs(a-f1):
    print(f1)
elif abs(a-f2)<abs(a-f1):
    print(f2)
elif abs(a-f2)==abs(a-f1):
    print(f2,f1)