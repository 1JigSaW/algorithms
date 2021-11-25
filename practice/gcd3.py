def gcd3(a, b):
	assert a >= 0 and b >= 0
	if a == 0 or b == 0:
		return max(a, b)
	elif a >= b:
		return gcd3(a % b, b)
	else:
		return gcd3(a, b % a)