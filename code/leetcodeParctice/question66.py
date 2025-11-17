"""
66. 加一
给定一个表示 大整数 的整数数组 digits,其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
将大整数加 1,并返回结果的数字数组。
"""

def plusOne(digits: list[int]) -> list[int]:
    if len(digits) == 0:
        return []
    ans = []
    addition = 1
    for i in range(len(digits) - 1, -1, -1):
        sum = (digits[i] + addition) % 10
        addition = (digits[i] + addition) // 10
        #print("digit[i] = {} add = {} sum = {}".format(digits[i], addition, sum))
        ans.append(sum)

    if addition != 0:
        ans.append(addition)

    left = 0
    right = len(ans) - 1
    while left < right:
        tmp = ans[left]
        ans[left] = ans[right]
        ans[right] = tmp
        left = left + 1
        right = right - 1

    return ans

def run():
    print(plusOne([4,3,2,1]))

if __name__ == "__main__":
    run()