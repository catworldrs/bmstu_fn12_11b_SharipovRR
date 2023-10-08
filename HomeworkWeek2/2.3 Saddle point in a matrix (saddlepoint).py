rows=int(input())
cols=int(input())
M=[]
for i in range(cols):
  M.append(list(map(int, input().split())))

def Saddles(matrix):
    rowmins = []
    rowmaxs = []
    colmins = []
    colmaxs = []

    for i,row in enumerate(matrix):
        m = min(row)
        M = max(row)
        for j,x in enumerate(row):
            if x == m: rowmins.append((i,j))
            if x == M: rowmaxs.append((i,j))

    t = [list(column) for column in zip(*matrix)]

    for j,col in enumerate(t): 
        m = min(col)
        M = max(col)
        for i,x in enumerate(col):
            if x == m: colmins.append((i,j))
            if x == M: colmaxs.append((i,j))
    return (set(rowmins) & set(colmaxs)) | (set(rowmaxs) & set(colmins))
print(Saddles(M))
