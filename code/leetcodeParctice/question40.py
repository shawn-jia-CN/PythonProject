"""
40. 组合总和 II
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 
"""

def dfs(used: dict[int:int], target: int, tmp: list[int], res: list[list[int]]) -> bool:
    #print("uesd = {} tmp = {} tar = {}".format(used, tmp, target))
    if target == 0:
        ans = tmp[:]
        ans.sort()
        if ans not in res:
            res.append(tmp[:])
        return True
    if target < 0:
        return False
    for num in used.keys():
        if num <= target and used[num] > 0:
            tmp.append(num)
            used[num] = used[num] - 1
            dfs(used, target - num, tmp, res)
            tmp.pop()
            used[num] = used[num] + 1
    return False

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    if len(candidates) <= 0:
        return res
    used = {}
    candidates.sort()
    for n in candidates:
        if n not in used:
            used[n] = 1
        else:
            used[n] = used[n] + 1
    dfs(used, target, [], res)
    return res


def run():
    print(combinationSum2([10,1,2,7,6,1,5], 8))


if __name__ == "__main__":
    run()