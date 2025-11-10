"""
39. 组合总和
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
"""

def dfs(candidates: list[int], target: int, res: list[list[int]], tmp: list[int], min: int) -> bool:
    if target == 0:
        res.append(tmp[:])
        return True
    if target < 0:
        return False
    for num in candidates:
        if num <= target and num >= min:
            tmp.append(num)
            dfs(candidates, target - num , res,  tmp, num)
            tmp.pop()
    return False

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    if len(candidates) <= 0:
        return res
    candidates.sort()
    dfs(candidates, target, res, [], candidates[0])
    return res




def run():
    print(combinationSum([2,3,5], 8))

if __name__ == "__main__":
    run()