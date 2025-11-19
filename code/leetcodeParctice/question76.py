"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
我实在写不出来了
"""
from collections import defaultdict
def minWindow(s: str, t: str) -> str:
    # 记录s对应元素与t的差异，少为正
    dict_difference = defaultdict(int)
    for c in t:
        dict_difference[c] += 1

    count_less = len(dict_difference)

    ans_l, ans_r = -1, len(s)
    cur_l = 0

    for cur_r, c in enumerate(s):
        # 遍历右指针 子串增加c，差异dict[c]-1，没有更新count_less
        dict_difference[c] -= 1
        # 如果从差异字典1变0，说明该字母数量相同，更新count_less-=1, 负变负，0变负数，正变正不更新count_less
        if dict_difference[c] == 0:
            count_less -= 1
        # 子数组覆盖t后 更新左指针，直到不覆盖
        while count_less == 0:
            if cur_r - cur_l < ans_r - ans_l:
                ans_l, ans_r = cur_l, cur_r

            x = s[cur_l]

            # 左指针移动，会引起差异dict变化
            dict_difference[x] += 1
            cur_l += 1

            # 如果差异dict[x]变成1了，说明不覆盖了     从-1变0，-变-，+变+这几种不影响count_less
            if dict_difference[x] == 1:
                count_less += 1

    return "" if ans_l < 0 else s[ans_l: ans_r + 1]

def run():
    s = "ADOBECODEBANC"
    t = "ABC"
    #s = "a"
    #t = "a"
    #s = "a"
    #t = "aa"
    #s = "ab"
    #t = "a"
    #s = "abc"
    #t = "b"
    #s = "bba"
    #t = "ab"
    print(minWindow(s, t))


if __name__ == "__main__":
    run()
    
 
