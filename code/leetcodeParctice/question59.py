"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""

def generateMatrix(n: int) -> list[list[int]]:
    if n <= 0:
        return []
    if  n == 1:
        return [[1]]
    m = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    roundMax = n // 2
    round = 0
    x = 0 + round
    y = 0 + round
    rawMax = n - 1 - round
    colMax = n - 1 - round
    rawMin = 0 + round
    colMin = 0 + round
    #print(roundMax)
    while round < roundMax:
        #print(round)
        x = 0 + round
        y = 0 + round
        rawMax = n - 1 - round
        colMax = n - 1 - round
        rawMin = 0 + round
        colMin = 0 + round        
        #print("x = {} y = {} rawMax = {} colMax = {} rawMin = {} colMin = {}".format(x, y, rawMax, colMax, rawMin, colMin))
        while y < colMax:
            m[x][y] = count
            count = count + 1
            y = y + 1
        #print("x = {} y = {} rawMax = {} colMax = {} rawMin = {} colMin = {}".format(x, y, rawMax, colMax, rawMin, colMin))
        while x < rawMax:
            m[x][y] = count
            count = count + 1    
            x = x + 1
        #print("x = {} y = {} rawMax = {} colMax = {} rawMin = {} colMin = {}".format(x, y, rawMax, colMax, rawMin, colMin))
        while y > rawMin:
            m[x][y] = count
            count = count + 1
            y = y - 1  
        #print("x = {} y = {} rawMax = {} colMax = {} rawMin = {} colMin = {}".format(x, y, rawMax, colMax, rawMin, colMin))
        while x > colMin:
            m[x][y] = count
            count = count + 1
            x = x - 1   
        round = round + 1

    #print("x = {} y = {} count = {}".format(x, y, count))
    if count <= n * n:
        x = 0 + round
        y = 0 + round
        m[x][y] = count
    return m

def run():
    l = generateMatrix(4)
    print(l)

if __name__ == "__main__":
    run()