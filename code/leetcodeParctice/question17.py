"""
17.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""

from collections import deque

def letterCombinations(digits: str) -> list[str]:
    map = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    res = []
    if len(digits) <= 0:
        return res
    queue = deque()
    for i in map[digits[0]]:
        queue.append(str(i))

    for index in range(1, len(digits)):
        tmp = map[digits[index]]
        count = len(queue)
        for i in range(count):
            s = queue.popleft()
            for a in tmp:
                queue.append(s + str(a))

    while len(queue) > 0:
        res.append(queue.popleft())
    return res


def run():
    print(letterCombinations("23"))


if __name__ == "__main__":
    run()