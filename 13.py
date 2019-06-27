ax=list(input())
a=len(ax)
b=[]
c=[]
if a%2==0:
    for i in range(0,a//2):
        b.append(ax[i])
    for i in range(a//2,a):
        c.append(ax[i])
else:
    for i in range(0,a//2):
        b.append(ax[i])
    for i in range(a//2+1,a):
        c.append(ax[i])
b.sort()
c.sort()
if b==c:
    print('YES')
else:
    print('NO')
