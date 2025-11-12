"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2,返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
"""

def addTwoStr(str1: str, str2: str):
    index = 0
    add = 0
    ans = ""
    while index < len(str1) and index < len(str2):
        sum = int(str1[index]) + int(str2[index]) + add
        if sum >= 10:
            add = 1
        else:
            add = 0
        ans = ans + str(sum%10)
        index = index + 1
    if index < len(str1):
        while index < len(str1):
            sum = add + int(str1[index])
            if sum >= 10:
                add = 1
            else:
                add = 0
            ans = ans + str(sum%10)
            index = index + 1
    if index < len(str2):
        while index < len(str2):
            sum = add + int(str2[index])
            if sum >= 10:
                add = 1
            else:
                add = 0
            ans = ans + str(sum%10)
            index = index + 1
    if add != 0:
        ans = ans + str(add)

    return ans





def multiply(num1: str, num2: str) -> str:
    res = []
    ans = ""
    if len(num1) <= 0 or len(num2) <= 0:
        return ""
    if num1 == "0" or num2 == "0":
        return "0"
    addtion = 0
    mul = 1
    tail = ""
    for index1 in range(len(num1) - 1, -1, -1):
        tmp = ""
        for index2 in range(len(num2) - 1, -1, -1):
            sum = int(num1[index1]) * int(num2[index2]) + addtion
            sumChar = sum % 10 
            addtion = int((sum - sumChar) / 10)
            tmp = tmp + str(sumChar)
        if addtion != 0:
            tmp = tmp + str(addtion)
            addtion = 0
        tmp = tail + tmp
        res.append(tmp[:])
        tail = tail + "0"
    print(res)
    if len(res) <= 0:
        return ""
    elif len(res) == 1:
        ans = res[0]
    else:
        ans = res[0]
        for index in range(1, len(res), 1):
            ans = addTwoStr(ans, res[index])
    ans1 = ""
    index = len(ans) - 1
    while(index >= 0 ):
        ans1 =  ans1 + ans[index]
        index = index - 1
    return ans1


def run():
    print(multiply("9133", "0"))


if __name__ == "__main__":
    run()