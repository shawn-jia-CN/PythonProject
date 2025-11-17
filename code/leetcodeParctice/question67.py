"""
67. 二进制求和
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
"""

def addBinary(a: str, b: str) -> str:
    if len(a) == 0 :
        return b
    if len(b) == 0:
        return a
    add = 0
    ans = ""
    startA = len(a) - 1
    startB = len(b) - 1
    while startA >= 0 and startB >= 0:
        numa = int(a[startA])
        numb = int(b[startB])
        sum = (numa + numb + add) % 2
        add = (numa + numb + add) // 2
        startA = startA - 1
        startB = startB - 1
        ans = str(sum) + ans
    #print("ans = {} add = {} startA = {} startB = {} ".format(ans, add, startA, startB))
    if startA >= 0:
        while startA >= 0:
            numa = int(a[startA])
            sum = (numa + add) % 2
            add = (numa + add) // 2
            startA = startA - 1
            ans = str(sum) + ans
    if startB >= 0:
        while startB >= 0:
            numb = int(b[startB])
            sum = (numb + add) % 2
            add = (numb + add) // 2
            startB = startB - 1
            ans = str(sum) + ans
    if add > 0:
        ans = str(add) + ans
    
    return ans

def run():
    print(addBinary("11", "1"))


if __name__ == "__main__":
    run()