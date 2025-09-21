"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
"""
def reverse(x: int) -> int:
    ans = 0
    f = 1
    if x < 0:
        x = x * -1
        f = -1
    if x == 0:
        return 0
    while (x != 0):
        tmp = x % 10
        ans = ans * 10 + tmp
        x = x // 10
    if -2**31 <=  ans * f <= 2**31-1:
        return ans * f  
    else:
        return 0

def run():
    tmp = 1534236469
    print(reverse(tmp))

if __name__ == "__main__":
    run()