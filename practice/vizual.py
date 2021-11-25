from matplotlib import pyplot as plt 

def compare(fs, args):
	for f in fs:
		plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
		plt.legend()
		plt.grid(True)

fib1 = old_fib1
compare([fib1, fib3], list(range(20)))