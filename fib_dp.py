from util import timed
from tqdm import tqdm


def fib(n):
    if n < 2:
        table[n] = n
        return n

    if table[n-1] is None:
        table[n-1] = fib(n-1)
    elif table[n-2] is None:
        table[n-2] = fib(n-2)
    return table[n-1] + table[n-2]


if __name__ == '__main__':
    N = 35
    print('N =', N)

    with timed():
        table = [None for i in range(N)]
        for i in tqdm(range(N)):
            fib(i)