#动态规划的0-1背包问题
def knapsack_01(weights, values, capacity):
    n = len(weights)
    # 创建 (n+1) x (capacity+1) 的 dp 表，初始化为0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(capacity + 1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    
    # 回溯找出选了哪些物品（可选）
    selected = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected.append(i-1)  # 物品编号从0开始
            j -= weights[i-1]
    
    return dp[n][capacity], selected[::-1]

# 示例
weights = [2, 3, 4, 5,2,3,4]
values  = [3, 4, 5, 6,4,2,1]
capacity = 12
max_value, selected_items = knapsack_01(weights, values, capacity)
print(f"最大价值: {max_value}")   # 输出 10
print(f"选中物品索引: {selected_items}")  # 输出 [0, 2] 即物品1和物品3