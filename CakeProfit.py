

def maxProfit(cakes, capacity, dp):
    if( dp[capacity] != -1):
        return dp[capacity]
    else:
        max_profit = 0
        for cake in cakes:
            value = cake[1]
            weight = cake[0]
            if( weight <= capacity):
                max_profit = max( max_profit, value + maxProfit(cakes, capacity - weight, dp))

        dp[capacity] = max_profit
        return max_profit


if __name__ == "__main__":
      cakes = [(7, 160), (3, 90), (2, 15)]
      capacity    = 0
      dp = [-1] * ( capacity + 1 )
      print maxProfit(cakes, capacity, dp)
