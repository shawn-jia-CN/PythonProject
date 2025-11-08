"""
16. 最接近的三数之和
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
"""


def threeSumClosest(nums: list[int], target: int) -> int:
    ret = 10**100
    sum = 0
    if len(nums) < 3:
        return None
    nums.sort()
    start = 0
    print("nums = {}".format(nums))
    while start < len(nums):
        if start > 0 and nums[start] == nums[start - 1]:
            start = start + 1
            continue
        left = start + 1
        right = len(nums) - 1
        print("start = {} left = {} right  = {}".format(start, left, right))
        while left < right :
            tmp = nums[start] + nums[left] + nums[right]
            print("tmp = {} ret = {} sum = {}".format(tmp, ret, sum))
            if tmp == target:
                return target
            elif tmp > target:
                if tmp - target < ret:
                    ret = tmp - target
                    sum = tmp
                right = right - 1
            else:
                if target - tmp < ret:
                    ret = target - tmp
                    sum = tmp
                left = left + 1
        start = start + 1
    return sum


def run():
    print(threeSumClosest([10,20,30,40,50,60,70,80,90],1))

if __name__ == "__main__":
    run()