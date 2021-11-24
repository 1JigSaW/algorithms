"""
Дано целое число 1 <= n <= 40, необходимо вычислить n-е число Фибоначчи
(напомним, что F_0=0, F_1=1, F_n=F_(n-1)+F_(n-2) при n>=2).

Sample Input:
3

Sample Output:
2
"""
def fib(n):
    fib_list = [0, 1]
    for num in range(2, n+1):
    	fib_list.append(fib_list[num-1] + fib_list[num-2])
    return fib_list[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

'''
a, b, n = 0, 1, int(input())
for i in range(2, n+1):
    a, b = b, a + b
    print(f'a = {a}, b = {b}')
print(b)
'''