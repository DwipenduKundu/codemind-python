l=int(input())
n=int(input())
for i in range(n):
    x,y=input().split()
    w,h=int(x),int(y)
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w==h and h>=l and w>=l:
        print("ACCEPTED")
    elif w>l or h>l:
        print("CROP IT")