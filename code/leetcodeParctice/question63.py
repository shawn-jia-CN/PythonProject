"""
63. 不同路径 II
给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。
网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。
返回机器人能够到达右下角的不同路径数量。
"""

def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
        return 0
    if len(obstacleGrid) == 1:
        if 1 in obstacleGrid[0]:
            return 0
        else:
            return 1
    if len(obstacleGrid[0]) == 1:
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                return 0
        return 1
    if (obstacleGrid[0][0] == 1 or obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1):
        return 0
    dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    dp[0][0] = 1
    for i in range(1, len(obstacleGrid[0]), 1):
        if obstacleGrid[0][i-1] == 1 or dp[0][i - 1] == 0:
            dp[0][i] = 0
        else:
            dp[0][i] = 1
    for j in range(1, len(obstacleGrid), 1):
        if obstacleGrid[j][0] == 1 or dp[j - 1][0] == 0:
            dp[j][0] = 0
        else:
            dp[j][0] = 1


    #print("len(obstacleGrid[0]) = {}".format(len(obstacleGrid[0])))
    #print(" len(obstacleGrid) = {}".format( len(obstacleGrid)))
    for i in range(1, len(obstacleGrid), 1):
        for j in range(1, len(obstacleGrid[0]), 1):
            #print("i = {} j = {}".format(i, j))
            if obstacleGrid[i][j - 1] != 1 and dp[i][j - 1] != 0:
                dp[i][j] = dp[i][j - 1] + dp[i][j]
            if obstacleGrid[i - 1][j] != 1 and dp[i - 1][j] != 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j]

    #print(dp)
    return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


def run():
    obstacleGrid = obstacleGrid =[[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
    print(uniquePathsWithObstacles(obstacleGrid))

if __name__ == "__main__":
    run()