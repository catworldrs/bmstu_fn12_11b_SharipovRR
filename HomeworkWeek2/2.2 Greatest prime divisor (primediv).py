n=int(input())
def sieveE(n):

    primeNUMS = [True] * (n+1)
    it = 0

    while it < n**0.5 :
        if it< 2:
            primeNUMS[it]= False

        elif primeNUMS[it]:
            for i in range(it*2, n+1, it):
                primeNUMS[i] = False

        it+=1

    return(x for x in range(n+1) if primeNUMS[x])
print(list(sieveE(n))[-1])
