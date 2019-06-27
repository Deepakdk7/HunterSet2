ax=int(input())
a=list(map(int,input().split()))
c=0
b=[]
d=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            c=c+1
            break
    else:
        b.append(a[i])        
print(*b)
print(max(a))
