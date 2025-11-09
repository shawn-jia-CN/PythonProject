"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除,要求 不使用 乘法、除法和取余运算。
整数除法应该向零截断,也就是截去(truncate)其小数部分。例如,8.345 将被截断为 8 ,-2.7335 将被截断至 -2 。
返回被除数 dividend 除以除数 divisor 得到的 商 。
注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [-231,  231 - 1] 。本题中，如果商 严格大于 231 - 1 ，则返回 231 - 1 ；如果商 严格小于 -231 ，则返回 -231 。

实在不想写了
"""

def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    a, b, res = abs(dividend), abs(divisor), 0
    for i in range(31, -1, -1):
        # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
        if (b << i) <= a:
            res += 1 << i
            a -= b << i
    return res if (dividend > 0) == (divisor > 0) else -res


def run():
    print(divide(10, 3))

if __name__ == "__main__":
    run()