a=int(input())
b=bin(int(input()))[2:]
m=int(input())
summa=0
summa+=int(b[0])*a
for i in range(1,len(b)):
    summa*=2
    summa+=a*int(b[i])
print(summa%m)
