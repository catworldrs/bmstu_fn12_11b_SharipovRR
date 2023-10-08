n=int(input())
arr=[int(input()) for i in range(n)]
k=int(input())
mx=sum(arr[:k])
sm=sum(arr[:k])
for i in range(k,n):
  sm-=arr[i-k]
  sm+=arr[i]
  mx=max(sm,mx)
print(mx)
