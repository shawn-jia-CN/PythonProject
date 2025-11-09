"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

def dfs(left :int , right : int , ret : str, ans : list[str]):
    print("left = {} right = {}, ret = {}".format(left, right, ret))
    if left == 0 and right == 0:
        ans.append(ret)
        return 
    if left > 0:
        dfs(left - 1, right, ret + "(", ans)
    if right > 0:
        if left < right:
            dfs(left, right - 1, ret + ")", ans)


def generateParenthesis(n: int) -> list[str]:
    ans : list[str] = []
    dfs(n, n, "", ans)
    return  ans 


def run():
    print(generateParenthesis(3))


if __name__ == "__main__":
    run()