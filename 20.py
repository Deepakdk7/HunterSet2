a,b=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in range(a,b+1):
    c.append(bin(i))
for i in c:
    e.append(i.count('1'))
for i in e:
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            d.append(i)
print(len(d))
