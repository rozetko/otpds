#!/usr/bin/python
# coding: utf-8

class MatrixMethod(object):
	def __init__(self, matrix):
		self.matrix = matrix
		for i, string in enumerate(self.matrix):
			self.matrix[i] = [int(digit) for digit in string]

		self.cols = len(self.matrix[0])
		self.rows = len(self.matrix)

		self.code = []

	def coding(self, information):
		information = [int(i) for i in information]
		redundantElements = [0 for _ in xrange(self.cols)]
		
		for j in xrange(self.cols):
			for i in xrange(self.rows):
				if self.matrix[i][j]:
					redundantElements[j] ^= information[i]

		self.code = information + redundantElements
		return self.code

	def decoding(self, errors):
		errors = [int(i) for i in errors]
		syndrome = [0 for _ in xrange(self.cols)]

		checkMatrix = self.matrix + generateIdentityMatrix(self.cols)
		code = self.makeErrors(errors)

		for j in xrange(self.cols):
			for i in xrange(self.cols + self.rows):
				if code[i]:
					syndrome[j] ^= checkMatrix[i][j]

		error = 0
		for element in syndrome:
			if element:
				error = 1
				break

		fixed = list(code)
		if not error:
			errorInfo = 'Нет ошибок'
		else:		
			if syndrome in checkMatrix:
				errorIndex = checkMatrix.index(syndrome)
				errorInfo = '1 ошибка: в %d элементе' %(errorIndex + 1)

				fixed[errorIndex] ^= 1
			else:
				indexMatrix, checkMatrix = generateCheckMatrixForTwoErrors(checkMatrix)
				if syndrome in checkMatrix:
					errorIndex = indexMatrix[checkMatrix.index(syndrome)]
					errorInfo = '2 ошибки: в %d и %d элементах' %(errorIndex[0] + 1, errorIndex[1] + 1)

					fixed[errorIndex[0]] ^= 1
					fixed[errorIndex[1]] ^= 1
				else:
					errorInfo = 'Больше 2 ошибок'

		return (errorInfo, code, fixed)

	def makeErrors(self, errors):
		code = list(self.code)

		for i, error in enumerate(errors, 0):
			if error:
				code[i] ^= 1

		return code

def generateIdentityMatrix(n):
	if n < 1:
		raise 'n must be >= 1'

	matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]

	for i in xrange(n):
		for j in xrange(n):
			if i == j:
				matrix[i][j] = 1
	return matrix

def generateCheckMatrixForTwoErrors(checkMatrix):
	def xorLists(a, b):
		if len(a) != len(b):
			raise 'Length of lists must be equal'
		
		length = len(a)

		result = [0 for _ in xrange(length)]
		for i in xrange(length):
			result[i] = a[i] ^ b[i]

		return result

	cols = len(checkMatrix[0])
	rows = len(checkMatrix)

	matrix = [[0 for _ in xrange(cols)] for _ in xrange(rows * (rows - 1))]
	indexMatrix = ['' for _ in xrange(rows * (rows - 1))]

	cur = 0
	for i in xrange(rows):
		for j in xrange(1, rows):
			indexMatrix[cur] = (i, j)
			matrix[cur] = xorLists(checkMatrix[i], checkMatrix[j])
			cur += 1

	return (indexMatrix, matrix)