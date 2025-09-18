import sys

# recursion approach 
def solve(values, weights, pos, weight_remain):
    # base case
    if pos == len(values):
        return 0
    
    # include this item
    total_val_include = -1
    if weight_remain - weights[pos] >= 0:
       total_val_include = solve(values, weights, pos + 1, weight_remain - weights[pos]) + values[pos]
    total_val_exclude = solve(values, weights, pos + 1, weight_remain)

    return max(total_val_exclude, total_val_include)

# dynamic programming 
def dp_solve(values, weights, max_weight):
    dp = [0 for i in range(max_weight + 1)]

    for i in range(len(values)):
        current_weight = weights[i]
        current_val = values[i]
        for j in range(max_weight, current_weight - 1, -1):
            dp[j] = max(dp[j], current_val + dp[j - current_weight])
    
    return dp[max_weight]

if __name__ == "__main__":
    values = input("values: ").split()
    weights = input("weights: ").split()
    w = input("maximum weight: ")

    max_val = solve(values, weights, 0, w)
    print(max_val)