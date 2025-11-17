"""
69. x 的平方根 
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""

def mySqrt(x: int) -> int:
    known_ans = {
        0: 0,
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2, 
        6: 2,
        7: 2,
        8: 2,
        9: 3
    }  
    if x in known_ans.keys():
        return known_ans[x]
    start = 9
    ans = 3
    old_ans = 2
    
    while start < x :
        #print("old_ans = {} ans = {} start = {} x = {}".format(old_ans, ans, start, x))
        start = start * start
        old_ans = ans
        ans =  ans * ans

    print("old_ans = {} ans = {} x = {}".format(old_ans, ans, x))
    while (old_ans < ans):
        mid = (old_ans + ans)//2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            if (mid - 1) * (mid - 1) < x:
                return mid - 1
            else:
                ans = mid
        else:
            if (mid + 1) * (mid + 1) > x:
                return mid
            else:
                old_ans = mid
    return mid

def run():
    print(mySqrt(1085817232))


if __name__ == "__main__":
    run()