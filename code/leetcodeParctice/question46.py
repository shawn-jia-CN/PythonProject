"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""

def dfs(nums: list[int], tmp:list[int] , used: list[int],  res:list[list[int]]) -> None:
    if len(tmp) == len(nums):
        res.append(tmp[:])
        return 
    for index in range(len(nums)):
        if not used[index]:
            tmp.append(nums[index])
            used[index] = True
            dfs(nums, tmp, used, res)
            tmp.pop()
            used[index] = False
    return 

def permute(nums: list[int]) -> list[list[int]]:
    res = []
    if len(nums) <= 0:
        return res
    if len(nums) == 1:
        return [nums]    
    used = [False] * len(nums)
    dfs(nums, [], used, res)
    return res

def run():
    print(permute([1,2,3]))

if __name__ == "__main__":
    run()