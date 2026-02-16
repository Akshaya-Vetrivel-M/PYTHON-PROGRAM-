A = [[5, 4, 3],  
    [2, 4, 6],
    [4, 7, 9],  
    [8, 1, 3]]  
transResult = [[0, 0, 0, 0],    
              [0, 0, 0, 0],
              [0, 0, 0, 0]]  
for a in range(len(A)):    
   for b in range(len(A[0])):    
          transResult[b][a] = A[a][b]       
print("The transpose of matrix A is: ")  
for res in transResult:    
   print(res) 

O/P:
The transpose of matrix A is: 
[5, 2, 4, 8]
[4, 4, 7, 1]
[3, 6, 9, 3]
