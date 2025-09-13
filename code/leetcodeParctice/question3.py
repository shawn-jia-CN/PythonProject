"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""

def lengthOfLongestSubstring(s):
    left = 0
    right = 1
    maxLength = 0
    currentLength = 0
    index = 0
    if (len(s) == 0 or len(s) == 1):
        return len(s)
    d = {}
    d[s[left]] = left
    maxLength = right - left
    while (left < len(s) and right < len(s)):
        if s[right] in d.keys() and d[s[right]] >= left:
            left = d[s[right]] + 1
            d[s[right]] = right
            right = right + 1
        else:
            d[s[right]] = right
            currentLength = right - left + 1
            right = right + 1
            if currentLength > maxLength:
                maxLength = currentLength

    return maxLength

def run():
   # nums = [2,7,11,15], target = 9
    input = "aab"
    print("ans = {}".format(lengthOfLongestSubstring(input)))
    return 

if __name__ == "__main__":
    run()