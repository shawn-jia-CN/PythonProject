"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。

我写不出来
"""
def isMatch(s: str, p: str) -> bool:
    m, n = len(s) + 1, len(p) + 1
    dp = [[False] * n for _ in range(m)]
    dp[0][0] = True
    # 初始化首行
    for j in range(2, n, 2):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            if p[j - 1] == '*':
                if dp[i][j - 2]: dp[i][j] = True                              # 1.
                elif dp[i - 1][j] and s[i - 1] == p[j - 2]: dp[i][j] = True   # 2.
                elif dp[i - 1][j] and p[j - 2] == '.': dp[i][j] = True        # 3.
            else:
                if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]: dp[i][j] = True # 1.
                elif dp[i - 1][j - 1] and p[j - 1] == '.': dp[i][j] = True    # 2.
    return dp[-1][-1]

def run():
    tmp = "ab"
    p = "a*"
    print(isPalindrome(tmp, p))

if __name__ == "__main__":
    run()