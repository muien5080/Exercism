def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    # Initialize DP array: dp[i] = fewest coins to make amount i
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    # Track which coin was used last for reconstruction
    prev = [-1] * (target + 1)

    for coin in coins:
        for amount in range(coin, target + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                prev[amount] = coin

    # If target is unreachable
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Reconstruct the coins used
    result = []
    curr = target
    while curr > 0:
        coin = prev[curr]
        result.append(coin)
        curr -= coin

    return sorted(result)