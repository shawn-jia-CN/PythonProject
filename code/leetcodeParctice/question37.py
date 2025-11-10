"""
编写一个程序，通过填充空格来解决数独问题。
数独的解法需 遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。
"""

def dfs(broad: list[list[int]], col: list[list[bool]], row: list[list[bool]], sub: list[list[list[bool]]], i: int , j:int) -> bool:
    if j == 9:
        i = i + 1
        j = 0
        if i == 9:
            return True
    if broad[i][j] == ".":
        for num in range(9):
            can_used =  col[i][num] and row[j][num] and sub[i//3][j//3][num]
            if can_used:
                col[i][num] = False
                row[j][num] = False
                sub[i//3][j//3][num] = False
                broad[i][j] = str(num + 1)
                if dfs(broad, col, row, sub, i, j+1):
                    return  True
                else:
                    col[i][num] = True
                    row[j][num] = True
                    sub[i//3][j//3][num] = True      
                    broad[i][j] = "."              
    else:
        return dfs(broad, col, row, sub, i, j+1)
    return False

def solveSudoku(board: list[list[str]]) -> None:
    col = [[True] * 9 for _ in range(9)] 
    row = [[True] * 9 for _ in range(9)] 
    sub = [[[True] * 9 for _ in range(3)] for _ in range(3)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                tmp = int(board[i][j]) - 1
                col[i][tmp] = False
                row[j][tmp] = False
                sub[i//3][j//3][tmp] = False
    dfs(board, col, row, sub, 0, 0)
    return 


def run():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    for l in board:
        print(l)
    solveSudoku(board)
    print("-"*45)
    for l in board:
        print(l)
    


if __name__ == "__main__":
    run()