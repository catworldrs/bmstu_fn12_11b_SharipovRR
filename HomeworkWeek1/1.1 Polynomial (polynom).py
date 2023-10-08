num=int(input())
x0=int(input())
summa=0
proizv=0
summa+=int(input())
for j in range(n-1):
    a=int(input())
    summa*=x0
    summa+=a
    proizv+=a*j
    proizv*=x0
print(summa,proizv)
