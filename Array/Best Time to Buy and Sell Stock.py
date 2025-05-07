"""You are given an array prices where prices[i] is the price of a stock on the i-th day. Find the maximum profit you can achieve. You may only buy once and sell once."""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))