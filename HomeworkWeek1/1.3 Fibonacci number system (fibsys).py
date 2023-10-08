x=int(input())
a=[]
while x>0:
 fm=0
 f0,f1=1,1
 index=0
 while fm<x:
  f0,f1=f1,f1+f0
  fm=f1
  index+=1
 a.append(index)
 x-=f0
f=['0']*max(a)
for i in a:
 f[i-1]='1'
f=''.join(f[::-1])
print(f)
