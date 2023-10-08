a=set(map(int, input().split()))
b=set(map(int,input().split()))
As=0
Bs=0
for i in a:
 As+=10**i
for i in b:
 Bs+=10**i
As,Bs=str(As),str(Bs)
As=int(As,2)
Bs=int(Bs,2)
print(As&Bs)
