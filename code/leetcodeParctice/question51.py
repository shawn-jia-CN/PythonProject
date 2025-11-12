"""
51. N 皇后
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""
def dfs(board: list[str], raw: list[bool], col: int, diag1: list[bool], diag2: list[bool], res: list[str], num: int, max: int) -> bool:
    if num == max:
        tmp = ""
        for s in board:
            for ss in s:
                tmp = tmp + ss
        if tmp not in res:
            res.append(tmp)
        return 
    for i in range(max):
            d1 = i - col + max - 1  # 主对角线索引
            d2 = i + col          # 副对角线索引
            if board[i][col] == "."  and raw[i] != True and diag1[d1] != True and diag2[d2] != True:
                board[i][col] = "Q"
                raw[i] = True
                diag1[d1] = True
                diag2[d2] = True
                dfs(board, raw, col + 1, diag1, diag2, res, num + 1, max)
                board[i][col] = "."
                raw[i] = False
                diag1[d1] = False
                diag2[d2] = False 

    return
        

def solveNQueens(n: int) -> list[list[str]]:
    if n == 0:
        return []
    if n == 1:
        return [["Q"]]
     
    res = []
    board = [["." for _ in range(n)] for _ in range(n)]
    raw: list[bool] = [False]* n
    diag1 = [False] * (2 * n - 1)    # 主对角线占用标记 (row - col + n - 1)
    diag2 = [False] * (2 * n - 1)    # 副对角线占用标记 (row + col)
    dfs(board, raw, 0, diag1 , diag2, res, 0, n)
    #print(res)
    ans = []
    for r in res:
        left = 0
        right = n 
        ans1 = []
        while right <= len(r):
            tmp = r[left: right]
            #print(tmp)
            ans1.append(tmp[:])
            left = right
            right = right + n
        ans.append(ans1)
    return ans

def run():
    res = solveNQueens(8)
    for r in res:
        print("-" * 20)
        print(r)
    return


if __name__ == "__main__":
    run()


