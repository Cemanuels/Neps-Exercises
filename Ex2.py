#sum couluns of a matrix 3x3
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_colun = [0, 0, 0]
for i in range(3):
	for j in range(3):
		n = int(input())
		matrix[i][j] = n
for colun in  range(3):
	for line in range(3):
		sum_colun[colun] += matrix[line][colun]
for i in range(3):
	print(f'Coluna {i}: {sum_colun[i]}')