alfavitEN =  'abcdefghijklmnopqrstuvwxyz'
len_alf = len(alfavitEN)
matrix = ['a']*len_alf
for i in range(len_alf):
    matrix[i] = ['a']*len_alf

for i in range(len_alf):
    for j in range(len_alf):
        matrix[i][j] = alfavitEN[j]

print(matrix)