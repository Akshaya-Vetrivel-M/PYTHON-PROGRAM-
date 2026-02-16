X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(x)

Output:
[118, 69, 60, 0]
[117, 68, 50, 0]
[113, 62, 57, 0]
