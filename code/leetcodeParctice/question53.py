"""
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""

def maxSubArray(nums: list[int]) -> int:
    f : list[int] = [nums[0]]
    max = f[0]
    for i in range(1, len(nums), 1):
        if nums[i] > f[i - 1] + nums[i]:
            f.append(nums[i])
        else:
            f.append(f[i - 1] + nums[i])
        if f[i] > max:
            max = f[i]
    return max


def run():  
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
    run()