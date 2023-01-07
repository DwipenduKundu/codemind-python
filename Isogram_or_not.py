str=input()
sl=list(str)
sl.sort()
ss=list(set(str))
ss.sort()
if ss==sl:
    print(True)
else:
    print(False)