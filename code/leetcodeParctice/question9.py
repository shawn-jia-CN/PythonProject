"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
"""
def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0  and x != 0):
        return False
    re = 0
    while ( x > re ) :
        re = re * 10 + x %10
        x = x // 10    
    return ( x == re or x == re // 10)


def run():
    #tmp = 123
    tmp = 121
    print(isPalindrome(tmp))

if __name__ == "__main__":
    run()
