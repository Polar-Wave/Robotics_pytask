def matrix_add(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    
    return result

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[9,8,7],
   [6,5,4],
   [3,2,1]]

for row in matrix_add(a,b):
    print(row)
