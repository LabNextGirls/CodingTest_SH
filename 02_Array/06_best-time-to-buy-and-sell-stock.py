# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

def maxProfit(prices):
    profit = 0
    min_time = prices.index(min(prices))
    max_time = prices.index(max(prices))

    if (max_time > min_time):
        profit = prices[max_time] - prices[min_time]
    else:
        temp_max = prices.index(max(prices[min_time::]))
        profit = prices[temp_max] - prices[min_time]

    return profit


prices = [7,6,4,3,1]
print(maxProfit(prices))

