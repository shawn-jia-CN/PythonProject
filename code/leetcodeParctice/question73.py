"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""

def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)

    for r in row:
        for i in range(len(matrix[0])):
            matrix[r][i] = 0
    for c in col:
        for i in range(len(matrix)):
            matrix[i][c] = 0
    return


def run():
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(matrix)
    print(matrix)


if __name__ == "__main__":
    run()