"""
38. 外观数列
「外观数列」是一个数位字符串序列，由递归公式定义：
countAndSay(1) = "1"
countAndSay(n) 是 countAndSay(n-1) 的行程长度编码。
行程长度编码(RLE)是一种字符串压缩方法，其工作原理是通过将连续相同字符（重复两次或更多次）替换为字符重复次数（运行长度）和字符的串联。例如，要压缩字符串 "3322251" ，我们将 "33" 用 "23" 替换，将 "222" 用 "32" 替换，将 "5" 用 "15" 替换并将 "1" 用 "11" 替换。因此压缩后字符串变为 "23321511"。
给定一个整数 n ，返回 外观数列 的第 n 个元素。
"""

def makeStr(s: str) -> str:
    seed = s[0]
    count = 1
    right = 1
    ret = ""
    while right < len(s):
        if s[right] == seed:
            count = count + 1
        else:
            ret = ret + str(count) + seed
            seed = s[right]
            count = 1
        right = right +1
    ret = ret + str(count) + seed
    return ret

def countAndSay(n: int) -> str:
    if n <= 0:
        return ""
    elif n == 1:
        return "1"
    else:
        return makeStr(countAndSay(n - 1))

def run():
    print(countAndSay(4))


if __name__ == "__main__":
    run()