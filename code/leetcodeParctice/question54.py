"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = []
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []
    if m == 1:
        return matrix[0]
    if n == 1:
        for index in range(m):
            ans.append(matrix[index][0])
        return ans
    x = 0
    y = 0
    maxCount = m * n
    round = 0
    count = 0
    rawMax = m - 1
    colMax = n - 1
    rawMin = 0
    rawMax = 0
    maxRound = min(m, n)//2
    while round < maxRound:
        x = 0 + round
        y = 0 + round
        rawMax = m - round - 1
        colMax = n - round - 1
        rawMin = 0 + round
        colMin = 0 + round
        #print("round = {} x = {} y = {} rawMax = {} colMax = {} ".format(round, x, y, rawMax, colMax))
        while y <= colMax - 1:
            ans.append(matrix[x][y])
            count = count + 1
            y = y + 1
        while x <= rawMax - 1:
            ans.append(matrix[x][y])
            count = count + 1
            x = x + 1
        while y >= colMin + 1:
            ans.append(matrix[x][y])
            count = count + 1
            y = y - 1
        while x >= colMin + 1:
            ans.append(matrix[x][y])
            count = count + 1
            x = x - 1
        round = round + 1

    if count < maxCount:
        x = 0 + round
        y = 0 + round
        rawMax = m - round - 1
        colMax = n - round - 1
        #print("m = {} n = {} ".format(m,n))
        #print("round = {} x = {} y = {} rawMax = {} colMax = {} ".format(round, x, y, rawMax, colMax))
        while x < rawMax:
            ans.append(matrix[x][y])
            x = x + 1
        while y < colMax:
            ans.append(matrix[x][y])
            y = y + 1
        ans.append(matrix[x][y])
    return ans

def run():
    #matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    #matrix = [[1]]
    matrix = [[3],[2]]
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
    matrix = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
    print(spiralOrder(matrix))


if __name__ == "__main__":
    run()