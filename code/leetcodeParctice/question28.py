"""
28. 找出字符串中第一个匹配项的下标
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
"""
def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack) :
        return -1
    
    if len(needle) == len(haystack) :
        if  needle == haystack:
            return 0
        else:
            return -1
    
    length = len(needle)
    for i in range(len(haystack) - length + 1):
        for j in range(length):
            if needle[j] != haystack[i + j]:
                break
        #print(" i = {} j = {} ".format(i, j))
        if j == length - 1 and needle[j] == haystack[i + j]:
            return i
    return -1

def run():
    print(strStr("leetcode", "leeto"))
    print(strStr("sadbutsad", "sad"))
    print(strStr("abc", "c"))

if __name__ == "__main__":
    run()
