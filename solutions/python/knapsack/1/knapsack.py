def maximum_value(maximum_weight, items):
    # dp[w] will store the maximum value for weight limit w
    dp = [0] * (maximum_weight + 1)
    
    for item in items:
        weight = item["weight"]
        value = item["value"]
        
        # Traverse backwards to ensure each item is only used once
        for w in range(maximum_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    return dp[maximum_weight]