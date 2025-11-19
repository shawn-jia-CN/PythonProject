"""
77. 组合
给定两个整数 n 和 k,返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
"""

def dfs(ans: list[list[int]], tmp: list[int], nums: list[int], used: list[bool], min: int, max: int):
    if len(tmp) == max:
        ans.append(tmp[:])
        return
    for i in range(len(nums)):
        if not used[i] and nums[i] > min :
            used[i] = True
            tmp.append(nums[i])
            dfs(ans, tmp, nums, used, nums[i], max)
            used[i] = False
            tmp.pop()
    return

def combine(n: int, k: int) -> list[list[int]]:
    if n == 0 or k == 0:
        return 0
    ans = []
    nums = []
    used = [False for _ in range(n)]
    for i in range(n):
        nums.append(i + 1)
    dfs(ans, [], nums, used, 0, k)
    return ans


def run():
    print(combine(4, 2))

if __name__ == "__main__":
    run()