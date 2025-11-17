"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""

def minPathSum(grid: list[list[int]]) -> int:
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, n, 1):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    
    for i in range(1, m, 1):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for i in range(1, m, 1):
        for j in range(1, n, 1):
            dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

def run():
    d = [[1,2,3],[4,5,6]]
    print(minPathSum(d))

if __name__ == "__main__":
    run()