"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""

def dfs(u: list[int], d: dict[int:int], tmp: list[int], res: list[list[int]], max: int) -> None:
    if len(tmp) == max:
        res.append(tmp[:])
        return
    for n in u:
        if d[n] > 0:
            tmp.append(n)
            d[n] = d[n] - 1
            dfs(u, d, tmp, res, max)
            tmp.pop()
            d[n] = d[n] + 1
    return

def permuteUnique(nums: list[int]) -> list[list[int]]:
    res = []
    if len(nums) == 0:
        return res
    if len(nums) == 1:
        return [nums]
    d = {}
    u = []
    for n in nums:
        if n in d.keys():
            d[n] = d[n] + 1
        else:
            d[n] = 1
            u.append(n)

    print(d)
    print(u)
    dfs(u, d, [], res, len(nums))
    return res 


def run():
    print(permuteUnique([1,1,2]))



if __name__ == "__main__":
    run()