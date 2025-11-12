"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""

def trap(height: list[int]) -> int:
    sum = 0
    if len(height) <= 2:
        return sum 
    N = len(height)
    left = [0] * N 
    left[0] = 0
    max = 0
    for index in range(0, len(height) - 1, 1):
        if height[index] > max:
            max = height[index]
        left[index + 1] = max
    right = [0] * N
    max = 0
    for index in range(N-1, 0, -1):
        if max < height[index]:
            max = height[index]
        right[index - 1] = max

    print("left = {}".format(left))
    print("right = {}".format(right))
    sum = 0
    for index in range(N):
        if height[index] < left[index] and height[index] < right[index]:
            if left[index] < right[index] :
                sum = left[index] - height[index] + sum
            else:
                sum = right[index] -height[index] + sum
    return sum


def run():
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))



if __name__ == "__main__":
    run()