t = int(input())
result = []
for i in range(t):
	n = int(input())
	s = input()
	for j in range(n):
		if s[j] == '8' and len(s) - (j+1) >= 11:
			result.append('YES')	
			break
		elif len(s) - (j+1) < 11:
			result.append('NO')
			break
for i in result:
	print(i)