"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。
"""
def longestValidParentheses(s: str) -> int:
    # left -> right
    if len(s) <= 1:
        return 0
    left = 0
    right = 0
    max = 0
    for i in range(len(s)):
        if s[i] == "(":
            left = left + 1
        else:
            right = right + 1
        if left < right:
            left = 0
            right = 0
        elif left == right:
            if 2 *right >  max:
                max = left + right
    # right -> left
    left = 0
    right = 0
    for i in range(len(s)-1, -1, -1 ):
        if s[i] == "(":
            left = left + 1
        else:
            right = right + 1
        if left > right:
            left = 0
            right = 0
        elif left == right:
            if left + right >  max:
                max = left + right
    return max



def run():
    print(longestValidParentheses("(()"))


if __name__ == "__main__":
    run()