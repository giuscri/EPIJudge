from test_framework import generic_test
from math import inf


def buy_and_sell_stock_once(prices):
    max_profit = -inf
    current_min_price = inf
    for price in prices:
        current_min_price = min(current_min_price, price)
        max_profit = max(price - current_min_price, max_profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
