# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices = [1,2]

def maxProfit(prices):
    profit = 0
    for i in range(0,len(prices)-1):
        if prices[i] < max(prices[i:len(prices)]):
            # print(profit)
            # print(prices[i])
            money = (max(prices[i:len(prices)]) - prices[i])
            if money > profit:
                profit = money
    return profit