n=int(input())
a=list(map(int,input().split()))
arev=a[::-1]
l=[]
l=arev[:len(arev)//2]+a[:len(a)//2]
for i in l:
    print(i,end=' ')