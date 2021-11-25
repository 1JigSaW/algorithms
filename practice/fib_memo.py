def memo(f):
	cache = {}
	def inner(n):
		if n not in cache:
			cache[n] = f[n]
		return cache[n]
	return inner

fib1 = memo(old_fib1)

print(fib1(80))