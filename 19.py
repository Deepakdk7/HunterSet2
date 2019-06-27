ax=list(map(int,input().split()))
n=int(ax[0])
k=int(ax[1])
a=[]
for i in range(0,n):
    a.append(input().split())
c=set(a[0])
for i in a:
    c=c & set(i)
d=list(c)
d.sort()
print(*d)
