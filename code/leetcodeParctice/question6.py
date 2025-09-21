"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
"""

def convert(s: str, numRows: int) -> str:
    if numRows < 2: return s
    ret = ["" for _ in range(numRows)]
    startRow = 0
    flag = -1
    for c in s:
        ret[startRow] += c
        if startRow == 0 or startRow == numRows - 1:
            flag = -1 * flag
        startRow = startRow + flag
    return "".join(ret)
        



def run():
    tmp = "PAYPALISHIRING"
    print(convert(tmp, 3))

if __name__ == "__main__":
    run()