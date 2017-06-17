from util import timed

coins = [1, 8, 10]
price = 17


def inspect():
    print("\t".join([str(i) for i in table]))


if __name__ == '__main__':
    # print header
    print("\t".join([str(i) for i in range(price+max(coins))]))
    print('_'*147)

    with timed():
        # initialize memo cache
        table = [float('inf') for i in range(price+max(coins))]
        table[0] = 0

        for i in range(price):
            inspect()
            for coin in coins:
                table[i+coin] = min(table[i+coin], table[i] + 1)

        inspect()

    print(f"In {', '.join(map(str, coins))} yen of coins, you can pay {price} yen for {table[price]} coins.")