n1,n2,n3=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
for i in range(n1+n2+n3):
    if sum(l1) == sum(l2) and sum(l2) == sum(l3):
        print(sum(l1))

        break
    else:
        if sum(l1)>sum(l2) and sum(l1)>sum(l3):
            l1.pop(0)
        elif sum(l2)>sum(l3):
            l2.pop(0)
        else:
            l3.pop(0)
