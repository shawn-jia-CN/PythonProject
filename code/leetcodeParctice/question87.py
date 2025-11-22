"""
使用下面描述的算法可以扰乱字符串 s 得到字符串 t :
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即,在执行这一步骤之后,s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2,判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。


实在不会了
"""

def isScramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False

    for i in range(1, len(s1)):
        if isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]) or \
                (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True
    return False

def run():
    s1 = "abcde"
    s2 = "caebd"
    print(isScramble(s1, s2))

if  __name__ == "__main__":
    run()