'''
Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5 , 
необходимо найти остаток от деления n-го числа Фибоначчи на m.

Sample Input:
10 2

Sample Output:
1
'''
def fib_mod(n, m):
    period = [0, 1]
    ind = 2
    while 2 < m * 6:
        period.append((period[ind - 1] + period[ind - 2]) % m)
        if period[ind] == 1 and period[ind - 1] == 0:
            break
        ind += 1
    return period[n % (len(period) - 2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))
 
 
if __name__ == "__main__":
    main()