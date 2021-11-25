def gcd2(a, b):
	while a and b:
		if a >= b:
			a %= b
		else:
			b %= a
	return max(a, b)