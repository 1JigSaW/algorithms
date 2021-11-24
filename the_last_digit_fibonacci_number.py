'''
Дано число 1 <= n <= 10^7, необходимо найти последнюю цифру nn-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно 
быть аккуратным с переполнением. В данной задаче, впрочем, этой проблемы можно избежать, 
поскольку нас интересует только последняя цифра числа Фибоначчи: 
если 0 <= a,b <= 9 — последние цифры чисел F_i и F_(i+1) 
соответственно, то (a+b)mod10 — последняя цифра числа F_(i+2) 

Sample Input:
841645

Sample Output:
5
'''
def fib_digit(n):
    fib_list = [0, 1]
    for num in range(2, n+1):
        fib_list.append((fib_list[num-1] + fib_list[num-2]) % 10)
    return fib_list[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
