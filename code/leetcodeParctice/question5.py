"""
给你一个字符串 s, 找到 s 中最长的 回文 子串。
"""

def longestPalindrome(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0 :
        return ""

    ans = ""
    maxLength = 0
    maxStart = 0
    for i in range(len(s)):
        #基数回文串
        l = i 
        r = i 
        while (l >= 0 and r < len(s)):
            if s[l] == s[r]:
                if (r - l) + 1 >= maxLength:
                    maxLength = r - l + 1
                    maxStart = l
                l = l - 1
                r = r + 1
            else:
                break
        
        #偶数回文串
        if i + 1 < len(s) and  s[i] == s[i + 1]:
            l = i 
            r = i + 1
            while (l >= 0 and r < len(s)):
                if s[l] == s[r]:
                    if (r - l) + 1 >= maxLength:
                        maxLength = r - l + 1
                        maxStart = l
                    l = l - 1
                    r = r + 1
                else:
                    break    
    ans = s[maxStart: maxStart +  maxLength]    
    return ans



def run():
    tmp = "cbbd"
    tmp = "babad"
    print(longestPalindrome(tmp))

if __name__ == "__main__":
    run()