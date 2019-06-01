matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
diag = [0, 0]
for i in range(3):
	for j in range(3):
		n = int(input())
		matrix[i][j] = n
		if i == j:
			diag[0] += matrix[i][j]
		if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
			diag[1] += matrix[i][j]
print(f'Diagonal principal: {diag[0]}')
print(f'Diagonal secundaria: {diag[1]}')  