n,d=map(int,input().split())
l=list(map(int,input().split()))
for i in range(d):
    k=l[0]
    l.remove(l[0])
    l.append(k)
for i in range(len(l)):
    print(l[i],end=" ")


