import numpy as np
def ColumnSum(matrix):
    
    column_sum_array=[]
    for i in range(row):
        sum=0
        for j in range(column):
            sum+=matrix[j][i]
        column_sum_array.append(sum)
    return column_sum_array
    
    
row =int(input("Enter row count: "))
column=int(input("enter column count:"))
array=list(map(int,input("enter matrix values: ").split()))
matrix=np.array(array).reshape(row,column)
print(ColumnSum(matrix))