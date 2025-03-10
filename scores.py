scores = [23, 45, 67, 32, 44, 47, 56, 76, 81, 90, 22, 78]

result = []
for score in scores:
	if score % 2 == 0:
		result.append(score)
print(result)
