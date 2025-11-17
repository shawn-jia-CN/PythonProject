"""
65. 有效数字
给定一个字符串 s ，返回 s 是否是一个 有效数字。
例如，下面的都是有效数字："2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"，而接下来的不是："abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"。
一般的，一个 有效数字 可以用以下的规则之一定义：
一个 整数 后面跟着一个 可选指数。
一个 十进制数 后面跟着一个 可选指数。
一个 整数 定义为一个 可选符号 '-' 或 '+' 后面跟着 数字。
一个 十进制数 定义为一个 可选符号 '-' 或 '+' 后面跟着下述规则：
数字 后跟着一个 小数点 .。
数字 后跟着一个 小数点 . 再跟着 数位。
一个 小数点 . 后跟着 数位。
指数 定义为指数符号 'e' 或 'E'，后面跟着一个 整数。
数字 定义为一个或多个数位。
"""

def isNumber(s: str) -> bool:
    if len(s) == 0:
        return False
    
    hasFlag = False
    hasE = False
    hasDig = False
    hasPoint = False

    dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(len(s)):
        if s[i] == "+" or s[i] == "-":
            if hasDig or hasPoint or hasFlag:
                return False
            hasFlag = True
            continue
        if s[i] == "e" or s[i] == "E":
            if i == len(s) - 1:
                return False
            if not hasDig:
                return False
            if hasE:
                return False
            hasDig = False
            hasFlag = False
            hasE = True
            hasPoint = False
            continue
        if s[i] == ".":
            if hasPoint :
                return False
            if hasE :
                return False
            hasPoint = True
            continue
        if s[i] not in dig :
            return False
        else:
            hasDig = True
            continue
    return hasDig

def run():
    print(isNumber("-1E+3"))


if __name__ == "__main__":
    run()