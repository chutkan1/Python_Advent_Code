def m(s):
	return s.count('(') - s.count(')')


def n(s):
	floor = 0
	index = 0
	for char in s:
		if (char == '('):
			floor += 1
		elif (char == ')'):
			floor -= 1
		index += 1
		if (floor < 0):
			return index