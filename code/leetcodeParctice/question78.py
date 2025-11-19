"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""

def dfs(nums: list[int], tmp: list[int], length: int, ans: list[list[int]], min: int):
    if len(tmp) == length:
        ans.append(tmp[:])
        return
    for i in range(len(nums)):
        if nums[i] > min:
            tmp.append(nums[i])
            dfs(nums, tmp, length, ans, nums[i])
            tmp.pop()
    return 

def subset(nums: list[int], length: int) -> list[list[int]]:
    ans = []
    used = [False for _ in range(len(nums))]
    dfs(nums,[], length, ans, nums[0] - 1)
    return ans

def subsets(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [[], nums]
    nums.sort()
    ans = [[]]
    for i in range(len(nums)):
        ans = ans + subset(nums, i + 1)
    return ans


def run():
    #nums = [4,1,0]
    nums = [1,2,3]
    print(subsets(nums))

if __name__ == "__main__":
    run()