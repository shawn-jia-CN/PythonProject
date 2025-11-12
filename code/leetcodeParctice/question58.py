"""
58. 最后一个单词的长度
给你一个字符串 s,由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
"""
def lengthOfLastWord(s: str) -> int:
    if len(s) <= 0:
        return 0
    count = 0
    for index in range(len(s) - 1, -1, -1):
        if s[index] == " ":
            if count == 0:
                continue
            else:
                return count
        else:
            count = count + 1
    return count


def run():
    print(lengthOfLastWord("Hello World"))

if __name__ == "__main__":
    run()
