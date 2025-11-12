"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数(即, xn ）。
"""
def myPowSingle(x: float, n: int) -> float:
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        ans = x 
        mi = 1
        while 2 * mi < n:
            ans = ans * ans
            #print("ans = {}".format(ans))
            mi = mi * 2
        #print("n = {}".format(n))
        #print("mi = {}".format(mi))
        if mi != n :
            diff = n - mi
            #print("diff = {}".format(diff))
            ans = myPowSingle(x, diff) * ans
    return ans

def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0.0
    else:
        if n == 0 :
            return 1.0
        elif n > 0 :
            return myPowSingle(x, n)
        else:
            return 1/myPowSingle(x, -1 * n)
    return 


def run():
    print(myPow(2.00,  -200000000))

if __name__ == "__main__":
    run()