"""
68. 文本左右对齐
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
注意:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0,小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
"""

def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    if len(words) <= 0  or maxWidth <= 0:
        return []
    ans: list[str] = []
    tmp = []
    current = 0
    for s in words:
        print("tmp = {} current = {} len(s) = {} s = {} ".format(tmp, current, len(s), s))
        if current + len(s) + len(tmp) <= maxWidth:
            tmp.append(s)
            current = current + len(s)            
        else:
            if current + len(tmp) - 1 == maxWidth:
                ans.append(" ".join(tmp))
            else:
                numOfSpance = maxWidth - current - len(tmp) + 1
                if len(tmp) == 1:
                    ans.append(tmp[0] + numOfSpance * " ")
                else:
                    k = 0
                    while numOfSpance > 0:
                        tmp[k%(len(tmp) - 1)] = tmp[k%(len(tmp) - 1)] + " "
                        k = k + 1
                        numOfSpance = numOfSpance - 1
                    ans.append(" ".join(tmp))
            tmp = []
            tmp.append(s)
            current = len(s)
    if len(tmp) > 0:
        print("tmp = {}".format(tmp))
        last = " ".join(tmp)
        ans.append(last + " "*(maxWidth - len(last)))
    return ans


def run():
    #words = ["This", "is", "an", "example", "of", "text", "justification."]
    #words = ["What","must","be","acknowledgment","shall","be"]
    words =["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    print(fullJustify(words, 16))

if __name__ == "__main__":
    run()