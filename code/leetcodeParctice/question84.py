"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
不想优化了
"""
def largestRectangleArea(heights: list[int]) -> int:
    if len(heights) <= 0:
        return 0
    left:list[int] = []
    leftIndex:list[int] = []
    right:list[int] = []
    rightIndex:list[int] = []
    print(heights)
    for i in range(len(heights)):
        while(len(leftIndex) > 0 and heights[leftIndex[-1]] >= heights[i]):
            leftIndex.pop()
        if len(leftIndex) == 0:
            left.append(-1)
        else:
            left.append(leftIndex[-1])
        leftIndex.append(i)
    for i in range(len(heights) - 1 , -1, -1):
        while(len(rightIndex) > 0 and heights[rightIndex[-1]] >= heights[i]):
            rightIndex.pop()
        if len(rightIndex) == 0:
            right.append(len(heights))
        else:
            right.append(rightIndex[-1])
        rightIndex.append(i)
    right.reverse()

    print("left = {}".format(left))
    print("right = {}".format(right))
    ans = 0
    for i in range(len(heights)):
        ans = max(ans, (right[i] - left[i] - 1)*heights[i])
    return ans

def run():
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))

if __name__ == "__main__":
    run()