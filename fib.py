from util import timed


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    N = 35
    print('N =', N)
    
    with timed():
        for i in range(N):
            print(fib(i))