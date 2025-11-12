"""
52. N 皇后 II
n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
"""

def dfs(board: list[str], raw: list[bool], diag1: list[bool], diag2: list[bool], col: int, ans: list[int], max: int):
    if col == max:
        ans.append(0)
        return 
    for i in range(max):
        d1 = i + col 
        d2 = i - col + max - 1
        if board[i][col] == "." and raw[i] == False and diag1[d1] == False and  diag2[d2] == False:
            board[i][col] = "Q"
            raw[i] = True
            diag1[d1] = True
            diag2[d2] = True
            dfs(board, raw, diag1, diag2, col+1, ans, max)
            board[i][col] = "."
            raw[i] = False
            diag1[d1] = False
            diag2[d2] = False     
    return       

def totalNQueens(n: int) -> int:
    if n <= 1:
        return n
    raw = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)
    board = [[ "." for _ in range(n)] for _ in range(n)]
    ans = []
    dfs(board, raw, diag1, diag2, 0, ans, n)
    return len(ans)

def run():
    print(totalNQueens(2))

if __name__ == "__main__":
    run()



