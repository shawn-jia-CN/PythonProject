"""
44. 通配符匹配
给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
实在不想写
"""

def isMatch(s: str, p: str) -> bool:
    
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    
    # 初始化
    dp[0][0] = True
    for j in range(1, n+1):     # p以*开头的情况
        if p[j-1] == '*':
            dp[0][j] = True
        else:
            break
    
    # 状态更新
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == p[j-1] or p[j-1] == '?':   # 条件1-2
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':                     # 条件3
                dp[i][j] = dp[i][j-1] | dp[i-1][j]  
    
    return dp[m][n]
    
def run():
    print(isMatch("aa", "a"))


if __name__ == "__main__":
    run()