"""
15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    if len(nums) <= 2:
        return res
    nums.sort()
    print(nums)
    start = 0
    while start < len(nums):
        if(start > 0 and nums[start]==nums[start - 1]):
            start = start + 1
            continue
        left = start + 1
        right = len(nums) - 1
        while (left < right):
            tmp = nums[start] + nums[left] + nums[right]
            if tmp == 0:
                res.append([nums[start], nums[left], nums[right]])
                while(left < right and nums[left]==nums[left + 1]):
                    left = left + 1
                while(left < right and nums[right]==nums[right - 1]):
                    right = right - 1
                left = left + 1
                right = right - 1
            elif tmp > 0:
                right = right - 1
            else:
                left = left + 1
        start = start + 1
    return res

def run():
    print(threeSum([-1,0,1,2,-1,-4]))

if __name__ == "__main__":
    run()