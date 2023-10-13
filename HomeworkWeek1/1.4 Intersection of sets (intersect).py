a=set(map(int, input().split()))
b=set(map(int,input().split()))
As=0
Bs=0
for i in a:
 As=As|int(str(10**i),2)
for i in b:
 Bs=Bs|int(str(10**i),2)
print(As&Bs)
