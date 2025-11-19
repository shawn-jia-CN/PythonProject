"""
74. 搜索二维矩阵
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
"""



def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    if m == 0 or n == 0:
        return False

    if m == 1:
        for i in range(n):
            if matrix[0][i] == target:
                return True
        return False

    if n == 1:
        for i in range(m):
            if matrix[i][0] == target:
                return True
        return False

    if matrix[0][0] > target:
        return False
    
    if matrix[m-1][n-1] < target:
        return False


    x = 0
    found = False
    for i in range(0, len(matrix), 1):  
        if matrix[i][0] == target:
            return True
        elif matrix[i][0] > target:
            x = i - 1
            found = True
            break
    if not found:
        x = len(matrix) - 1
    #print("x = {}".format(x))
    for i in range(0,len(matrix[0]), 1):
        if matrix[x][i] == target:
            return True
    return False

def run():
    #matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    #matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 30
    print(searchMatrix(matrix, target))


if __name__ == "__main__":
    run()