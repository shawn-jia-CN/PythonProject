"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入:strs = ["flower","flow","flight"]
输出："fl"
示例 2:
输入:strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 如果非空，则仅由小写英文字母组成
"""
def common(a: str, b:str) -> str:
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
            i = i + 1
            j = j + 1
        else:
            break

    return "".join(c)

def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    if len(strs) == 1:
        return strs[0]
    res = strs[0]
    for s in strs:
        res = common(res, s)
    return res



def run():
    print(longestCommonPrefix(["flower","flow","flight"]))

if __name__ == "__main__":
    run()




