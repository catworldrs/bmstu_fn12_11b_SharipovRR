n,k = map(int,(input()))                                                                                                           

answer = 0

for i in range(2, n + 1):
  
    answer+=(k - 1) % (i - 1)
  
    answer = answer % (i - 1) + 1 
  
print(answer)
