"""
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""
def largestRectangleArea(heights: list[int]) -> int:
    if len(heights) <= 0:
        return 0
    left: list[int] = []
    right: list[int] = []
    leftIndex: list[int] = []
    rightIndex: list[int] = []

    for i in range(len(heights)):
        while(len(leftIndex) > 0 and heights[leftIndex[-1]] >= heights[i]):
            leftIndex.pop()
        if len(leftIndex) == 0:
            left.append(-1)
        else:
            left.append(leftIndex[-1])
        leftIndex.append(i)
    
    #print(heights)
    for i in range(len(heights)-1, -1, -1):
        while(len(rightIndex) > 0 and heights[rightIndex[-1]] >= heights[i]):
            rightIndex.pop()
        if len(rightIndex) == 0:
            right.append(len(heights))
        else:
            right.append(rightIndex[-1])
        rightIndex.append(i)
    right.reverse()
    #print("heights = {}".format(heights))
    #print("left = {}".format(left))
    #print("right = {}".format(right))
    ans = 0
    for i in range(len(heights)):
        ans = max(ans, (right[i] - left[i] - 1) * heights[i])
    return ans

def maximalRectangle(matrix: list[list[str]]) -> int:
    if len(matrix) == 0:
        return 0
    if len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    h = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                h[i][j] = int(matrix[i][j])
            else:
                if int(matrix[i][j]) == 0:
                    h[i][j] = 0
                else:
                    h[i][j] = int(matrix[i][j]) + h[i - 1][j]
    ans = 0
    for i in range(m):
        ans = max(ans, largestRectangleArea(h[i]))
        #print(ans)

    return ans



def run():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    #matrix = [["0","1"],["1","0"]]
    print(maximalRectangle(matrix))

if __name__ == "__main__":
    run()