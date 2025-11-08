"""
给定一个只包括 '(',')','{','}', '[', ']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""

"""
type 1  保存 (
type 2  保存 [
type 3  保存 {
"""

from collections import deque

def isValid(s: str) -> bool:
    queue = deque()
    for i in s:
        if i == "(":
            queue.append(i)
        elif i == "[":
            queue.append(i)
        elif i == "{":
            queue.append(i)      
        elif i == ")":
            if len(queue) <= 0 or queue.pop() != "(":
                return False
        elif i == "]":
            if len(queue) <= 0 or queue.pop() != "[":
                return False
        else:
            if len(queue) <= 0 or queue.pop() != "{":
                return False
    return len(queue) == 0


def run():
    print(isValid("((()))[]("))


if __name__ == "__main__":
    run()