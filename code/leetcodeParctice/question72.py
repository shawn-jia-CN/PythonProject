"""
72. 编辑距离
给你两个单词 word1 和 word2, 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""

def minDistance(word1: str, word2: str) -> int:
    l1 = len(word1)
    l2 = len(word2)
    if l1 == 0 or l2 == 0:
        return max(l1, l2)

    dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
    dp[0][0] = 0
    for i in range(1, l1+1, 1):
        dp[0][i] = i
    for i in range(1, l2+1, 1):
        dp[i][0] = i
    
    for i in range(1, l2+1, 1):
        for j in range(1, l1+1, 1):
            if word2[i-1] == word1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

    return dp[l2][l1]
        

def run():
    print(minDistance("horse", "ros"))

if __name__ == "__main__":
    run()
