"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""
def uniquePaths(m: int, n: int) -> int:
    if m == 0 or n == 0 :
        return 0
    if m == 1 or n == 1:
        return 1
    ans = 0
    dp = [[0 for _ in range (n)] for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    
    for i in range(1, m, 1):
        for j in range(1, n, 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #print(dp)
    return dp[m-1][n-1]

def run():
    print(uniquePaths(3, 7))

if __name__ == "__main__":
    run()

