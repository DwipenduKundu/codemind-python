n=int(input())
np2=n+1
while str(np2)!=str(np2)[::-1]:
    np2+=1
np1=n-1
while str(np1)!=str(np1)[::-1]:
    np1-=1
if abs(n-np1)==abs(n-np2):
    print(np1,np2)
elif abs(n-np1)>abs(n-np2):
    print(np2)
else:
    print(np1)