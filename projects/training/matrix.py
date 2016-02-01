def matrix_scheme(n):
	matrix = []

	for i in range(n):
		new_matrix = []

		for j in range(n):
			new_matrix.append(0)

		matrix.append(new_matrix)

	return matrix


def print_matrix(matrix):
	for row in matrix:
		for element in row:
			print "%02d" % element,
		print


def horizontal_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for row in range(n):
		for element in range(n):
			matrix[row][element] = number
			number += 1

	return matrix


def vertical_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for element in range(n):
		for col in range(n):
			matrix[col][element] = number
			number += 1

	return matrix


def reverse_horizontal_matrix(n):
	matrix = matrix_scheme(n)
	number = n * n

	for row in range(n):
		for element in range(n):
			matrix[row][element] = number
			number -= 1

	return matrix


def reverse_vertical_matrix(n):
	matrix = matrix_scheme(n)
	number = n * n

	for element in range(n):
		for col in range(n):
			matrix[col][element] = number
			number -= 1

	return matrix


def horizontal_split_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for row in range(n):
		for element in range(n):
			if row == 0 or row % 2 == 0:
				matrix[row][element] = number
			else:
				matrix[row][(n - 1) - element] = number
			number += 1

	return matrix


def reverse_horizontal_split_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for row in range(n):
		for element in range(n):
			if row == 0 or row % 2 == 0:
				matrix[row][(n - 1) - element] = number
			else:
				matrix[row][element] = number
			number += 1

	return matrix


def vertical_split_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for element in range(n):
		for col in range(n):
			if element == 0 or element % 2 == 0:
				matrix[col][element] = number
			else:
				matrix[(n - 1) - col][element] = number
			number += 1

	return matrix


def reverse_vertical_split_matrix(n):
	matrix = matrix_scheme(n)
	number = 1

	for element in range(n):
		for col in range(n):
			if element == 0 or element % 2 == 0:
				matrix[(n - 1) - col][element] = number
			else:
				matrix[col][element] = number
			number += 1

	return matrix


print '\n''Horizontal matrix:'
matrix = horizontal_matrix(5)
print_matrix(matrix)


print '\n''Reverse horizontal matrix:'
matrix = reverse_horizontal_matrix(5)
print_matrix(matrix)


print '\n''Horizontal split matrix:'
matrix = horizontal_split_matrix(5)
print_matrix(matrix)


print '\n''Reverse horizontal split matrix:'
matrix = reverse_horizontal_split_matrix(5)
print_matrix(matrix)


print '\n''Vertical matrix:'
matrix = vertical_matrix(5)
print_matrix(matrix)


print '\n''Reverse vertical matrix:'
matrix = reverse_vertical_matrix(5)
print_matrix(matrix)


print '\n''Vertical split matrix:'
matrix = vertical_split_matrix(5)
print_matrix(matrix)


print '\n''Reverse vertical split matrix:'
matrix = reverse_vertical_split_matrix(5)
print_matrix(matrix)

"""
pri python raboti array[0][0]

gledai print fuknciqta, mnogo podobno e
joker 3 polzvai range()

"""
