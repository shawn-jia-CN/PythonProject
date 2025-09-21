"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
函数 myAtoi(string s) 的算法如下：
空格：读入字符串并丢弃无用的前导空格（" "）
符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
返回整数作为最终结果。
"""

def myAtoi(s: str) -> int:
    ans = 0
    pos = 1
    has_nums = False
    has_pos = False
    for c in s.strip():
        if c == "+":
            if has_nums or has_pos:
                break
            else:
                has_pos = True
                continue
        elif c == "-" :
            if has_nums or has_pos:
                break
            else:
                has_pos = True
                pos = -1
                continue
        elif c in "0123456789":
            has_nums = True
            ans = int(c) + ans * 10
        else:
            break
    if -2 ** 31 <= ans * pos <= 2**31 -1:
        return ans * pos
    elif pos == 1:
        return 2**31 -1
    else:
        return -2 ** 31
    
def run():
    tmp = "123"
    print(myAtoi(tmp))

if __name__ == "__main__":
    run()