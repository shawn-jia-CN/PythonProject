"""
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
实在优化不动了
"""
def strToDict(s: str) -> dict[str: int]:
    d = {}
    for n in s:
        if n in d.keys():
            d[n] = d[n] + 1
        else:
            d[n] = 1
    return d

def isSame(d1: dict[str: int], d2: dict[str: int]):
    if len(d1.keys()) != len(d2.keys()):
        return False
    if d1.keys() != d2.keys():
        return False
    for k in d1.keys():
        if d1[k] != d2[k]:
            return False
    return True

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    if len(strs) <= 0:
        return []
    elif len(strs) == 1:
        return [strs]
    else:
        ans = []
        dictList : list[dict[str: int]] = []
        for s in strs:
            dictList.append(strToDict(s))
        used : list[bool] = [False] * len(strs)
        num = 0
        while num < len(strs):
            for index in range(len(strs)):
                tmp = []
                if used[index] != True:
                    used[index] = True
                    num = num + 1
                    tmp.append(strs[index])
                    i = index + 1
                    #print("index = {} strs[index] = {}".format(index, strs[index]) )
                    #print(strs[index])
                    while i < len(strs):
                        if used[i] != True:
                            #print(strs[i])
                            if isSame(dictList[i], dictList[index]):
                                used[i] = True
                                tmp.append(strs[i])
                                num = num + 1
                        i = i + 1
                    ans.append(tmp[:])
    return ans

def run():
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

if __name__ == "__main__":
    run()