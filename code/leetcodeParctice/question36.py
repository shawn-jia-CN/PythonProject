"""
36. 有效的数独
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
"""

def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        check = [False] * 9
        for j in range(9):
            if board[i][j] == ".":
                continue
            else:
                if check[int(board[i][j]) - 1] != False:
                    return False
                else:
                    check[int(board[i][j]) - 1] = True

    for j in range(9):
        check = [False] * 9
        for i in range(9):
            if board[i][j] == ".":
                continue
            else:
                if check[int(board[i][j]) - 1] != False:
                    return False
                else:
                    check[int(board[i][j]) - 1] = True

    for i in range(3):
        for j in range(3):
            check = [False] * 9
            for m in range(i * 3, i * 3 + 3, 1):
                for n in range(j * 3, j * 3 + 3, 1):
                    if board[m][n] == ".":
                        continue
                    else:
                        if check[int(board[m][n]) - 1] != False:
                            return False
                        else:
                            check[int(board[m][n]) - 1] = True
    return True

def run():
    board =  [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))

if __name__ == "__main__":
    run()

