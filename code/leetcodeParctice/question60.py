"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k,返回第 k 个排列。
实在不想优化了
"""
def dfs(num: list[int], tmp :list[int], ans: list[list[int]], used: list[int],  count:int , target: int):
    if len(tmp) == len(used):
        ans.append(tmp[:])
        count = count + 1
        return 
    for index in range(len(num)):
        if used[index] != True and count < target:
            used[index] = True
            tmp.append(num[index])
            dfs(num, tmp, ans, used, count, target)
            used[index] = False
            tmp.pop()
    return 

def getPermutation(n: int, k: int) -> str:
    if n <= 0:
        return ""
    num = []
    ans = []
    ret = ""
    tmp = []
    used = [False] * n
    for i in range(n):
        num.append(i + 1)
    dfs(num, tmp, ans, used, 0, k)
    for a in ans[k - 1]:
        ret = ret + str(a)
    return ret


def run():
    print(getPermutation(3, 3))


if __name__ == "__main__":
    run()
