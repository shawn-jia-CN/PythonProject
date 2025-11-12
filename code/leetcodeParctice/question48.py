"""
48. 旋转图像
给定一个 n * n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""

def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    tmp : list[list[int]] = []
    for n in matrix:
        tmp.append(n[:])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[j][i] = tmp[len(matrix[i])-1-i][j]
    return 


def run():
    m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(m)
    print(m)



if __name__ == "__main__":
    run()

    