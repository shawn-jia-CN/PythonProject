"""
90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
"""

def dfs(keys: list[int], d: dict[int:int],target: int, tmp:list[int], ans:list[list[int]]):
    print("d = {} keys = {}, tar = {} tmp = {} ans = {}".format(d, keys, target, tmp, ans))
    if len(tmp) == target:
        ans.append(tmp[:])
    for i in keys:
        if d[i] > 0 and (len(tmp) == 0  or (len(tmp) != 0 and i >= tmp[-1])):
            tmp.append(i)
            d[i] = d[i] - 1
            dfs(keys, d, target, tmp, ans)
            tmp.pop()
            d[i] = d[i] + 1
    return

def defsubsetWithDupK(keys: list[int], d: dict[int: int], k: int) -> list[list[int]]:
    ans: list[list[int]] = []
    dfs(keys, d, k, [], ans)
    return ans

def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [[], nums]
    else:
        ans = [[], nums]
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] = d[n] + 1
            else:
                d[n] = 1


        keys = []
        for k in d.keys():
            keys.append(k)
        keys.sort()

        for i in range(1, len(nums), 1):
            print("i = {}".format(i))
            ans = ans + defsubsetWithDupK(keys, d, i)
        return ans

def run():
    nums = [1,2,2]
    print(subsetsWithDup(nums))

if __name__ == "__main__":
    run()